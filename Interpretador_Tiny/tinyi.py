import argparse

from Syntatic.SyntaticAnalysis import SyntaticAnalysis

def main():
  parser = argparse.ArgumentParser(description="Tiny Interpreter")
  parser.add_argument("input_file", help="Path to the Tiny program file")

  args = parser.parse_args()

  try:
    syntactic = SyntaticAnalysis()
    syntactic.inicio(args.input_file).execute()
  
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
