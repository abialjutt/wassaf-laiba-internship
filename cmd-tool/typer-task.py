import typer
app =  typer.Typer()
# num_of_line=4
x=int(input("Enter number to print lines "))

@app.command()
def writeTo(file):
    try:
        with open(file, "r+") as f:
            counter = 1
            for line in f:
                counter = counter+1
                print(f.readline())
                if counter>x:
                    break
    except TypeError:
        print(TypeError)

if __name__ == "__main__":
    app()
