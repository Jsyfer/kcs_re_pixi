import argparse
from pathlib import Path

from database import initialize_and_load_data, DB_PATH


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Initialize the SQLite database and load KCS mock JSON data."
    )
    parser.add_argument(
        "--data-dir",
        default=Path(__file__).resolve().parent / "api" / "kcsapi",
        type=Path,
        help="Root folder containing the mock API JSON files.",
    )
    parser.add_argument(
        "--db-path",
        default=DB_PATH,
        type=Path,
        help="SQLite database file path.",
    )
    args = parser.parse_args()

    getdata_path = args.data_dir / "api_start2" / "getData.json"
    require_info_path = args.data_dir / "api_get_member" / "require_info.json"
    port_path = args.data_dir / "api_port" / "port.json"

    if (
        not getdata_path.exists()
        or not require_info_path.exists()
        or not port_path.exists()
    ):
        raise FileNotFoundError(
            "Please ensure getData.json, require_info.json and port.json exist under api/kcsapi/."
        )

    conn = initialize_and_load_data(
        getdata_path, require_info_path, port_path, args.db_path
    )
    print(f"Database initialized at {args.db_path}")
    conn.close()


if __name__ == "__main__":
    main()
