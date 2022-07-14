import typer
app =  typer.Typer()

@app.command()
def writeTo(file):
    try:
        with open(file, "r+") as f:
            print(f.read())
    except TypeError:
        print("File not Found")

if __name__ == "__main__":
    app()
