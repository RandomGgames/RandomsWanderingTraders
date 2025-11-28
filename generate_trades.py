import json
import logging
import pathlib
import socket
import sys
import time
import toml
import traceback
import typing
from datetime import datetime

logger = logging.getLogger(__name__)

"""
Python Script Template

Template includes:
- Configurable logging via config file
- Script run time at the end of execution
- Error handling and cleanup
"""

__version__ = "1.0.0"  # Major.Minor.Patch


def read_toml(file_path: typing.Union[str, pathlib.Path]) -> dict:
    """
    Read configuration settings from the TOML file.
    """
    file_path = pathlib.Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    config = toml.load(file_path)
    return config


def load_module(module_name: str):
    return __import__(module_name)


def write_text_file_lines(file_path: typing.Union[str, pathlib.Path], lines: typing.List[str]) -> None:
    """
    Writes a list of strings to a text file, with each string on a new line.
    Includes error checking and logging.

    Args:
    file_path (typing.Union[str, pathlib.Path]): The file path of the text file to write.
    lines (typing.List[str]): A list of strings to write to the text file.

    Returns:
    None
    """
    try:
        with open(file_path, 'w') as f:
            for line in lines:
                f.write(line + '\n')
        logger.info(f"Successfully wrote {file_path}")
    except Exception as e:
        logger.error(f"Error writing {file_path}: {e}")


def generate_scoreboard_commands(trade_sections: dict) -> list[str]:
    commands = []
    index = 1

    for section in trade_sections.values():
        trades = section["trades"]
        max_qty = section["maximum_quantity"]

        count = len(trades)
        start = index
        end = index + count - 1

        for _ in range(max_qty):
            commands.append(
                f"execute store result score @s RandomsWanderingTraders run random value {start}..{end}"
            )
            commands.append(
                "execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade"
            )

        index = end + 1

    return commands


def generate_trade_commands(trade_sections: dict) -> list[str]:
    commands = []
    index = 1

    for section in trade_sections.values():
        for trade in section["trades"]:
            commands.append(
                f"execute if score @s RandomsWanderingTraders matches {index} "
                f"unless data entity @s Offers.Recipes.[{trade.unless_nbt()}] "
                f"run data modify entity @s Offers.Recipes insert -1 value {trade.add_nbt()}"
            )
            index += 1

    return commands


def export_scoreboard_commands(trade_sections: dict, output_path: typing.Union[str, pathlib.Path]):
    lines = generate_scoreboard_commands(trade_sections)
    write_text_file_lines(output_path, lines)


def export_trade_commands(trade_sections: dict, output_path: typing.Union[str, pathlib.Path]):
    lines = generate_trade_commands(trade_sections)
    write_text_file_lines(output_path, lines)


def export_all(trade_sections, scoreboard_path, trades_path):
    export_scoreboard_commands(trade_sections, scoreboard_path)
    export_trade_commands(trade_sections, trades_path)


def main():
    trade_sections = load_module("trades").trades

    scoreboard_cmds = generate_scoreboard_commands(trade_sections)
    trade_cmds = generate_trade_commands(trade_sections)

    logger.info("SCOREBOARD COMMANDS:")
    for c in scoreboard_cmds:
        logger.info(c)

    logger.info("\nTRADE COMMANDS:")
    for c in trade_cmds:
        logger.info(c)

    export_all(
        trade_sections,
        config.get("output", {}).get("scoreboard_commands_path", "scoreboard_commands.txt"),
        config.get("output", {}).get("trade_commands_path", "trade_commands.txt")
    )


def format_duration_long(duration_seconds: float) -> str:
    """
    Format duration in a human-friendly way, showing only the two largest non-zero units.
    For durations >= 1s, do not show microseconds or nanoseconds.
    For durations >= 1m, do not show milliseconds.
    """
    ns = int(duration_seconds * 1_000_000_000)
    units = [
        ('y', 365 * 24 * 60 * 60 * 1_000_000_000),
        ('mo', 30 * 24 * 60 * 60 * 1_000_000_000),
        ('d', 24 * 60 * 60 * 1_000_000_000),
        ('h', 60 * 60 * 1_000_000_000),
        ('m', 60 * 1_000_000_000),
        ('s', 1_000_000_000),
        ('ms', 1_000_000),
        ('us', 1_000),
        ('ns', 1),
    ]
    parts = []
    for name, factor in units:
        value, ns = divmod(ns, factor)
        if value:
            parts.append(f"{value}{name}")
        # Stop after two largest non-zero units
        if len(parts) == 2:
            break
    if not parts:
        return "0s"
    return "".join(parts)


def setup_logging(
        logger: logging.Logger,
        log_file_path: typing.Union[str, pathlib.Path],
        number_of_logs_to_keep: typing.Union[int, None] = None,
        console_logging_level: int = logging.DEBUG,
        file_logging_level: int = logging.DEBUG,
        log_message_format: str = "%(asctime)s.%(msecs)03d %(levelname)s [%(funcName)s] [%(name)s]: %(message)s",
        date_format: str = "%Y-%m-%d %H:%M:%S") -> None:
    log_file_path = pathlib.Path(log_file_path)
    log_dir = log_file_path.parent
    log_dir.mkdir(parents=True, exist_ok=True)

    # Limit # of logs in logs folder
    if number_of_logs_to_keep is not None:
        log_files = sorted([f for f in log_dir.glob("*.log")], key=lambda f: f.stat().st_mtime)
        if len(log_files) > number_of_logs_to_keep:
            for file in log_files[:-number_of_logs_to_keep]:
                file.unlink()

    # Clear old handlers to avoid duplication
    logger.handlers.clear()
    logger.setLevel(file_logging_level)

    formatter = logging.Formatter(log_message_format, datefmt=date_format)

    # File Handler
    file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    file_handler.setLevel(file_logging_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_logging_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


if __name__ == "__main__":
    config_path = pathlib.Path("config.toml")
    if not config_path.exists():
        raise FileNotFoundError(f"Missing {config_path}")
    global config
    config = read_toml(config_path)

    console_logging_level = getattr(logging, config.get("logging", {}).get("console_logging_level", "INFO").upper(), logging.DEBUG)
    file_logging_level = getattr(logging, config.get("logging", {}).get("file_logging_level", "INFO").upper(), logging.DEBUG)
    logs_file_path = config.get("logging", {}).get("logs_file_path", "logs")
    use_logs_folder = config.get("logging", {}).get("use_logs_folder", True)
    number_of_logs_to_keep = config.get("logging", {}).get("number_of_logs_to_keep", 10)
    log_message_format = config.get("logging", {}).get(
        "log_message_format",
        "%(asctime)s.%(msecs)03d %(levelname)s [%(funcName)s]: %(message)s"
    )

    script_name = pathlib.Path(__file__).stem
    pc_name = socket.gethostname()
    if use_logs_folder:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_dir = pathlib.Path(f"{logs_file_path}/{script_name}")
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file_name = f"{timestamp}_{script_name}_{pc_name}.log"
        log_file_path = log_dir / log_file_name
    else:
        log_file_path = pathlib.Path(f"{script_name}_{pc_name}.log")

    setup_logging(
        logger,
        log_file_path,
        console_logging_level=console_logging_level,
        file_logging_level=file_logging_level,
        number_of_logs_to_keep=number_of_logs_to_keep,
        log_message_format=log_message_format
    )

    error = 0
    try:
        start_time = time.perf_counter_ns()
        logger.info(f"Script: {script_name} | Version: {__version__} | Host: {pc_name}")

        main()
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        duration = format_duration_long(duration / 1e9)
        logger.info(f"Execution completed in {duration}.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted by user.")
        error = 130
    except Exception as e:
        logger.warning(f"A fatal error has occurred: {repr(e)}\n{traceback.format_exc()}")
        error = 1
    finally:
        for handler in logger.handlers:
            handler.close()
        logger.handlers.clear()
        sys.exit(error)
