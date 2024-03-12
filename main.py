import os
import subprocess

is_reducer = os.environ.get("IS_REDUCER")
print(f"is_reducer: {is_reducer}")

if __name__ == "__main__":
    os.makedirs(os.path.join(os.getcwd(), "data", "counts"), exist_ok=True)

    if is_reducer == "0":
        subprocess.run(
            ["uvicorn", "map:app", "--host", "0.0.0.0", "--port", "80"], check=True
        )

    else:  # is_reducer = 1
        subprocess.run(["python", "reduce.py"], check=True)
        # print("Reducer is not implemented yet")
