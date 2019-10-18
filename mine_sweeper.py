from mine_sweeper_core import MineSweeper
import argparse

def main():
	parser = argparse.ArgumentParser(description="Mine Sweeper")
	parser.add_argument("-d","--debug",action="store_true",help="debug mode")
	parser.add_argument("-e","--easy",action="store_true",help="difficulty : easy")
	parser.add_argument("-n","--normal",action="store_true",help="difficulty : normal")
	parser.add_argument("-s","--sticky",action="store_true",help="difficulty : hard")
	args = parser.parse_args()

	mine_sweeper = MineSweeper(args)
	mine_sweeper.loop()

if __name__ == "__main__":
    main()