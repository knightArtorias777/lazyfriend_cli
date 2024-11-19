import typer
from script.down_file import t1down_file

app = typer.Typer()


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
async def download(softname:str):
    print("exec command download")
    await t1down_file


if __name__ == "__main__":
    app()
