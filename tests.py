import pytest


def run_all_tests():
    # Directory where your test files are located
    # Replace with your tests directory path if different
    test_dir = "src/datascience/tests"

    # Run pytest with the specified directory
    exit_code = pytest.main([test_dir])

    if exit_code == 0:
        print("All tests passed successfully!")
    else:
        print(f"Some tests failed. Exit code: {exit_code}")


if __name__ == "__main__":
    run_all_tests()
