import argparse 

if __name__ == "__main__":
    print("Run Chansey Run!")

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--screen", required=False, type=str, default=None, help="name of screen under test, if omitted -> Full Screen")
    args = parser.parse_args()

    print(f"screen under test: {args.screen}")



