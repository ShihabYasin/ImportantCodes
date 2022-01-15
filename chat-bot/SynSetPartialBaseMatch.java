package oneWordOneLiner_Concept_DB;

import java.io.IOException;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Locale;
import java.util.Random;
import java.util.Scanner;

public class SynSetPartialBaseMatch {

	public int getQueryString(String qstr) throws IOException {

		// System.out.println("Enter One Small One Liner Related to Sysnset.");
		Random rand = new Random();
		File file = new File(
				"/home/tigerit/Desktop/OneWordLinerConcept_DBase/src/oneWordOneLiner_Concept_DB/synset_5_.txt");
		// File file_out = new
		// File("/home/shihab/Desktop/OneLiner/src/StaticResponseFilter/out.txt");

		// FileWriter fileWriter = new FileWriter(file_out);
		Scanner scanner = null;
		String userInputString = "";
		String synDetected = "";
		int randomNum;

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
				if ((splitted_lineFromFile[i]).contains(userInputString)) {
					temp += lineFromFile;
					break;
				}
			}
		}

		String[] splitted = temp.split("\\s*,\\s*");
		String[] t = new String[splitted.length];
		int cnt_t = 0;
		for (int i = 0; i < splitted.length; i++) {
			if (splitted[i].contains(userInputString)) {
				t[cnt_t] = splitted[i];
				cnt_t++;
			}
		}

		String[] synset = new String[splitted.length];

		int cnt = 0;
		for (int i = 0; i < cnt_t; i++) {
			if (t[i].startsWith(userInputString) && t[i] != "" && t[i] != null && !t[i].isEmpty()) {
				if (t[i] != "") {
					synset[cnt] = t[i];
					cnt++;
				}				
			}
		}
		for (int i = 0; i < cnt; i++) {
			// System.out.println(synset[i]);
		}

		if (cnt > 0) { /// If synset exists
			// getting a synonymous representation other than query term
			randomNum = rand.nextInt(cnt + 1);
			synDetected = synset[randomNum];

			// Impression Design Section
			randomNum = rand.nextInt(8);
			switch (randomNum) {
			case 1:
				System.out.println("Hmm " + synDetected + " has similar spelling part");
				break;
			case 2:
				System.out.println("I can also say " + synDetected);
				break;
			case 3:
				System.out.println("May be you like to say " + synDetected);
				break;
			case 4:
				System.out.println("Much the same letters as " + synDetected);
				break;
			case 5:
				System.out.println("Other related saying you can say " + synDetected);
				break;
			case 6:
				System.out.println("You can also say " + synDetected);
				break;
			case 7:
				System.out.println("Frog's mind crossed with another idea  " + synDetected);
				break;
			case 0:
				System.out.println("Another comparable saying " + synDetected);
				break;
			}
			scanner.close();
			return 1;
		} else {

			System.out.print("You can spell it like ");
			for (int counter = 0; counter < userInputString.length(); counter += 1) {
				System.out.print(userInputString.charAt(counter) + " ");
			}
			System.out.println();
			scanner.close();
			return -1;
		}

	}

}
