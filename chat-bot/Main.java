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

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);

		int ret = 0;

		while (true) {

			System.out.println("Enter a Small One Liner: ( _quit to exit. )");
			String userInputString = scanner.nextLine();
			if (userInputString.equals("_quit")) {
				System.out.println("PROGRAM EXITED.");
				return;
			}

			SynSetBasedMatch synbm = new SynSetBasedMatch();
			ret = synbm.getQueryString(userInputString);
			if (ret == -1) {
				SenticBasedMatch sbm = new SenticBasedMatch();
				ret = sbm.getQueryString(userInputString); // -1 for UNDETECTED, +1 FOR DETECTED SUCCESSFULLY
				if (ret == -1) {
					SynSetPartialBaseMatch synPbm = new SynSetPartialBaseMatch();
					ret = synPbm.getQueryString(userInputString); // -1 for UNDETECTED, +1 FOR DETECTED SUCCESSFULLY
				}
			}

			if (ret == -1) {

				System.out.println("MOOD: UNDETECTED !!!");

			}

		}

	}

}
