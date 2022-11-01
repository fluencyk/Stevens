/**
School: Stevens Institute of Technology
Topic: Practice of Chapter 8, 9
* * *
Implemented: 27/10/2022
Coder Name: Yujun Kong
Enrolled Class: CS-501_WS
Description: File Analyzing and Content Sorting
*/

package Project_05;

import java.io.*;
import java.util.*;

public class InputFile {
	
	private static String inFilePath;
	private static String[] inFileWords;
	
	/** default constructor */
	public InputFile() {
		
	}
	
	/** overloaded constructor with arguments */
	public InputFile(String fileName) {
		
		inFilePath = "src/Project_05/" + fileName;
		inFileWords = null;
		processWords();
	}
	
	// setter method
	private static void processWords() {
		
		String singLine = "";
		File inFile = new File(inFilePath);
		
		try (
			Scanner in = new Scanner(inFile);
		){
			while (in.hasNext()) {
				String line = in.nextLine().strip();
				String eachWord = "";
				for (int i = 0; i < line.length(); i++) {
					if (!Character.isAlphabetic(line.charAt(i)) && line.charAt(i) != ' ') {
						continue;
					} else {
						eachWord = eachWord + line.charAt(i);
					}
				}
				singLine = singLine + " " + eachWord;
			}
			
			in.close();
		} catch (FileNotFoundException e) {
			//e.printStackTrace();
			System.out.println("No such file! Program ends.");
			System.exit(0);
		}
		
		inFileWords = singLine.strip().split(" ");
	}
	
	// getter method
	public String[] getWords() {
		
		return inFileWords;
	}
	
	/** program entrance, manual testing */
	public static void main(String[] args) { // !<- manual testing case, DO NOT regard this as main program entrance!
		
		InputFile manualTestCase_outPurifiedWords = new InputFile("inPoem.txt");
		
		System.out.println(Arrays.toString(manualTestCase_outPurifiedWords.getWords()));
	}

} /** end of programming */
