package oneWordOneLiner_Concept_DB;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Scanner;

public class SenticBasedMatch {

	public int getQueryString(String qstr) throws FileNotFoundException {

		// TODO Auto-generated method stub
		Random rand = new Random();
		File file = new File("/home/tigerit/Desktop/OneWordLinerConcept_DBase/senticnet5.txt");
		File file_out = new File("/home/tigerit/Desktop/OneWordLinerConcept_DBase/out.txt");

		Scanner scanner = null;
		String userInputString = "";
		int randomNum;

		userInputString = qstr;
		userInputString = userInputString.toLowerCase().trim();
		userInputString = userInputString.replaceAll(" ", "_");

		String temp = "";
		scanner = new Scanner(file);
		int matchFound = 0;
		while (scanner.hasNextLine()) {
			String lineFromFile = scanner.nextLine();

			String[] splitted_lineFromFile = lineFromFile.split("\\s+");
			double val = Double.parseDouble(splitted_lineFromFile[2]);
			String modifier = "";

			if (-1 <= val && val <= -0.5) {
				modifier = "extremely";
			} else if (-0.5 < val && val <= 0) {
				modifier = "very";
			} else if (val > 0 && val <= 0.5) {
				modifier = "very";
			} else if (val > 0.5 && val <= 1) {
				modifier = "extremely";
			}

			if (splitted_lineFromFile[0].equals(userInputString)) {
				randomNum = rand.nextInt(4);
				switch (randomNum) {
				case 0:
					System.out.println("I think its " + modifier + " " + splitted_lineFromFile[1] + " to say that");
					break;
				case 1:
					System.out.println("I guess its " + modifier + " " + splitted_lineFromFile[1] + " to speak that");
					break;
				case 2:
					System.out.println("Probably its " + modifier + " " + splitted_lineFromFile[1] + " to utter that");
					break;
				case 3:
					System.out.println("May be its " + modifier + " " + splitted_lineFromFile[1] + " to claim that");
					break;
				}

				matchFound = 1;

			}

		}
		scanner.close();
		if (matchFound == 0) {
			// System.out.println("UNDETECTED");
			return -1;
		} else {
			return 1;
		}
		
	}

}
