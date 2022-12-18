/**
 * School: Stevens Institute of Technology
 * Topic: Practice of Chapter 8, 9
 * * *
 * Implemented: 11/30/2022
 * Coder Name: Yujun Kong
 * Enrolled Class: CS-501_WS
 * Description: Inheritance Techniques
 */

package Project_07;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class DtrAndCpr {
	
	private static String inFilePath;
	
	protected static String directorName;
	protected static String composerName;
	protected ArrayList<String> stdbyLines = new ArrayList<String>();
	
	/** default constructor, currently using */
	public DtrAndCpr() {
		
	}
	
	/** manual testing for checking any list */
	@SuppressWarnings("unused")
	private static void manualTestPrint(Object obj) {
		
		int size = 0;
		if (obj instanceof ArrayList) {
			size = ((ArrayList<?>) obj).size();
		}
		for (int i = 0; i < size; i++) {
			System.out.println(((ArrayList<?>) obj).get(i));
		}
	}
	
	// setter of movies' director name 
	protected void setDtrName(String dtrName) {
		
		directorName = dtrName;
	}
	
	// getter of movies' director name
	public String getDtrName() {
		
		return directorName;
	}
	
	// setter of movies' composer name
	protected void setCprName(String cprName) {
		
		composerName = cprName;
	}
	
	// getter of movies' composer name
	public String getCprName() {
		
		return composerName;
	}
	
	// setter of targeted input file's path defining
	protected void setInFilePath(String fileName) {
		
		inFilePath = "src/Project_07/" + fileName;
	}
	
	// getter of targeted input file's path defining
	public String getInFilePath() {
		
		return inFilePath;
	}
	
	// processes input file
	protected void prcsInFileToStdbyLines() {
		
		ArrayList<String> lines = new ArrayList<String>();
		File inFile = new File(getInFilePath());
		try (Scanner in = new Scanner(inFile)){
			while (in.hasNext()) {
				lines.add(in.nextLine());
			}
		} catch (FileNotFoundException e) {
			System.out.println("No such file! Program ends.");
			System.exit(0);
		}
		this.stdbyLines = lines;
	}
	
	/** program entrance, <- manual testing case, DO NOT regard this as main program entrance! */
	// uncomment below for testing manually
	public static void main(String[] args) {
		
		/* DtrAndCpr superClass = new DtrAndCpr();
		superClass.setInFilePath("MovieListing.txt");
		superClass.prcsInFileToStdbyLines();
		manualTestPrint(superClass.stdbyLines); */
	}

}
