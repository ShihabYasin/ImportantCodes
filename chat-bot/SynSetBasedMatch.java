package oneWordOneLiner_Concept_DB;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class SynSetBasedMatch {

	public int getQueryString(String qstr) throws IOException {

		Random rand = new Random();
		File file = new File(
				"/home/tigerit/Desktop/OneWordLinerConcept_DBase/src/oneWordOneLiner_Concept_DB/synset_5_.txt");
		//File file_out = new File("/home/tigerit/Desktop/JAVA_PROJECT_ONE_WORD/JAVA_PROJECT_ONE_WORD/OneLiner/src/StaticResponseFilter/out.txt");

		//File file_prod = new File("/home/tigerit/Desktop/JAVA_PROJECT_ONE_WORD/JAVA_PROJECT_ONE_WORD/OneLiner/src/StaticResponseFilter/prod_one_liner.txt");

		//FileWriter fileWriter = new FileWriter(file_out);
		Scanner scanner_prod = null;
		Scanner scanner = null;
		String userInputString = "";
		String synDetected = "";
		int randomNum;
		// scanner_prod = new Scanner(file_prod);

		// while (scanner_prod.hasNextLine()) {

		// userInputString = "every year";

		userInputString = qstr;

		String temp = "";
		scanner = new Scanner(file);
		while (scanner.hasNextLine()) {
			String lineFromFile = scanner.nextLine();
			// System.out.println("NextLine: " + lineFromFile );
			String[] splitted_lineFromFile = lineFromFile.split("\\s*,\\s*");

			for (int i = 0; i < splitted_lineFromFile.length; i++) {
				// System.out.println(splitted_lineFromFile[i]);
			}

			for (int i = 0; i < splitted_lineFromFile.length; i++) {
				if (userInputString.equals(splitted_lineFromFile[i])) {
					temp += lineFromFile;
					break;
				}
			}
		}

		String[] splitted = temp.split("\\s*,\\s*");
		String[] synset = new String[splitted.length];

		int cnt = 0;
		for (int i = 0; i < splitted.length; i++) {
			if (!userInputString.equals(splitted[i]) && splitted[i] != "") {
				synset[cnt] = splitted[i];
				cnt++;
			}
		}

		if (cnt > 0) { /// If synset exists
			// getting a synonymous representation other than query term
			randomNum = rand.nextInt(cnt + 1);
			synDetected = synset[randomNum];

			// Impression Design Section
			randomNum = rand.nextInt(8);
			switch (randomNum) {
			case 1:
				System.out.println("I think its similar to " + synDetected);
				break;
			case 2:
				System.out.println("You can also say " + synDetected);
				break;
			case 3:
				System.out.println("I guess its comparable to " + synDetected);
				break;
			case 4:
				System.out.println("Probably its much the same as " + synDetected);
				break;
			case 5:
				System.out.println("Other related saying you can say " + synDetected);
				break;
			case 6:
				System.out.println("Frog is thinking that its comparable to " + synDetected);
				break;
			case 7:
				System.out.println("Frog's mind crossed with a similar idea  " + synDetected);
				break;
			case 0:
				System.out.println("Frog knows it you can also speak " + synDetected);
				break;
			}
			scanner.close();
			return 1;
		} else {
			scanner.close();
			return -1;
			/// System.out.println("UNDETECTED");

		}

	}
}
