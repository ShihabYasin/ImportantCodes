package oneWordOneLiner_Concept_DB;
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
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter One Small One Liner Related to Sysnset.");
		Random rand = new Random();
		File file = new File(
				"/home/tigerit/Desktop/OneWordLinerConcept_DB/senticnet5.txt");
		File file_out = new File(
				"/home/tigerit/Desktop/OneWordLinerConcept_DB/out.txt");

		FileWriter fileWriter = new FileWriter(file_out);
		Scanner scanner = null;
		String userInputString = "";
		String synDetected = "";
		int randomNum;

		while (true) {
			// userInputString = "every year";
			System.out.println("Enter a Small One Liner: (  _quit to exit.  )");
			scanner = new Scanner(System.in);
			userInputString = scanner.nextLine();
			userInputString = userInputString.toLowerCase();

			if (userInputString.equals("_quit")) {
				break;
			}

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
			} else {
				System.out.println("UNDETECTED");
			}

		} /// While Loop: Session

		scanner.close();
		fileWriter.flush();
		fileWriter.close();
		System.out.println("\n\n\n\nPROGRAM ENDED");
	}

}
