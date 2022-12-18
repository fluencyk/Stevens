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

import java.awt.Font;
import java.util.*;
import javax.swing.*;

public class ShowSortedMovieInfoByGenre {
	
	/** Instantiates movie class, providing inherited object's method */
	private static Movie movie = new Movie();
	
	/** declares array list for holding sorted movie list */
	private static ArrayList<String[]> srtdMovieListByGenre = new ArrayList<String[]>();
	
	/** initiates a variable field for holding genre title */
	private static String genreTitle;
	
	/** initiates general user input value */
	private static String optionInput;
	
	/** handles while loop for processing user input */
	private static boolean isValid;
	
	/** default constructor */
	public ShowSortedMovieInfoByGenre() {
		/** standby for use */
	}

	/** overloaded constructor */
	public ShowSortedMovieInfoByGenre(String targetFileName) {		
		movie.setInFilePath(targetFileName);
	}
	
	/** manual testing for checking any list */
	public static void manualTestPrint(ArrayList<String[]> lst) {
		
		for (int i = 0; i < lst.size(); i++) {
			System.out.println(Arrays.toString(lst.get(i)));
		}
		System.out.println();
	} /** manual test case for specifically printing inspection needed list */
	
	// gets unsorted movie list by genre chosen
	private static ArrayList<String[]> getUnsrtdMovieListByGenre(String genreName) {
		
		genreTitle = genreName;
		ArrayList<String[]> unsrtdMovieListByGenre = new ArrayList<String[]>();
		
		for (int i = 2; i < movie.stdbyLines.size(); i++) {
			String[] movieInfoByGenre = new String[3];
			movie.setMovieInfo(movie.stdbyLines.get(i));
			movieInfoByGenre[0] = movie.getMovieTitle();
			movieInfoByGenre[1] = movie.getYearReleased();
			movieInfoByGenre[2] = movie.getRating();
			
			if (genreName.equals(movie.getGenre())) {
				unsrtdMovieListByGenre.add(movieInfoByGenre);
			}
		}		
		return unsrtdMovieListByGenre;
	}
	
	// determines if two items can be swapping applicable
	private static boolean isSwapAppicable(String objOne, String objTwo) {
		
		String strOne = objOne.replace("'", "").replace(".", "").replace(" ", "");
		String strTwo = objTwo.replace("'", "").replace(".", "").replace(" ", "");
		
		int min = 0;
		if (strOne.length() == strTwo.length()) {
			min = strOne.length();
		} else if (strOne.length() < strTwo.length()) {
			min = strOne.length();
		} else if (strOne.length() > strTwo.length()) {
			min = strTwo.length();
		}
		
		int i = 0;
		for (int j = 0; j < min; j++) {
			if(strOne.charAt(i) - 0 == strTwo.charAt(i) - 0) {
				i++;
			} else if (strOne.charAt(i) - 0 > strTwo.charAt(i) - 0) {
				return true;
			} else {
				return false;
			}
		}		
		return false;
	}
	
	// sorts unsorted movie list
	private static void setSrtdMovieListByGenre(ArrayList<String[]> arrLst) {
		
		String[] tempArr = new String[3];
		for (int i = 0; i < arrLst.size(); i++) {
			for (int j = i + 1; j < arrLst.size(); j++) {
				if (isSwapAppicable(arrLst.get(i)[1], arrLst.get(j)[1])) {
					tempArr = arrLst.get(j);
					arrLst.set(j, arrLst.get(i));
					arrLst.set(i, tempArr);
				} else if (arrLst.get(i)[1].equals(arrLst.get(j)[1]) 
					&& isSwapAppicable(arrLst.get(i)[0], arrLst.get(j)[0])) {
					tempArr = arrLst.get(j);
					arrLst.set(j, arrLst.get(i));
					arrLst.set(i, tempArr);
				}
			}
		}
		srtdMovieListByGenre = arrLst;
	}
	
	//
	public ArrayList<String[]> getSrtdMovieListByGenre(){
		
		return srtdMovieListByGenre;
	}
	
	/** below are user experience flow methods, above are algorithms in logic */
	
	// shows sorted movie list by chosen genre
	private static void showMoviesByGenreUI() {
		
		String contentHeader = new String(
			" Director: " + movie.getDtrName() + "\n" +
			" Composer: " + movie.getCprName() + "\n\n" +
			" Genre: " + genreTitle + "\n\n");
		
		ArrayList<Integer> sizeArr = new ArrayList<Integer>();
		for (int x = 0; x < srtdMovieListByGenre.size(); x++) {
			sizeArr.add(srtdMovieListByGenre.get(x)[0].length());
		} int maxSizeNum = Collections.max(sizeArr);
		
		int labelLen = 0;
		int altLen = 0;
		if (maxSizeNum < 11) {
			labelLen = maxSizeNum + 10 - 11;
			altLen = 15;
		} else if (maxSizeNum > 11) {
			labelLen = maxSizeNum - 11 + 10;
			altLen = 15;
		}
		
		
		String columnLabels = new String(
			" Movie Title" + dynamicBlank(labelLen) + "Year Released" + dynamicBlank(10) + "Rating \n");
		
		StringBuilder movieInfoLines = new StringBuilder("");
		for (int k = 0; k < srtdMovieListByGenre.size(); k++) {
			StringBuilder currLine = new StringBuilder("");
			currLine.append(srtdMovieListByGenre.get(k)[0]);
			if (srtdMovieListByGenre.get(k)[0].length() == maxSizeNum) {
				currLine.append(dynamicBlank(altLen));
			} else if (srtdMovieListByGenre.get(k)[0].length() < maxSizeNum) {
				currLine.append(dynamicBlank(maxSizeNum - srtdMovieListByGenre.get(k)[0].length() + altLen));
			}
			currLine.append(srtdMovieListByGenre.get(k)[1]);
			currLine.append(dynamicBlank(14));
			currLine.append(srtdMovieListByGenre.get(k)[2]);
			currLine.append("\n");
			movieInfoLines.append(" " + currLine.toString());
		}
		
		String contentBody = new String(
			columnLabels +
			movieInfoLines
			);
		
		JTextArea textArea = new JTextArea(
			contentHeader +
			contentBody);
		
		textArea.setFont(new java.awt.Font("monospaced", Font.PLAIN, 14));         
        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        scrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED);
		
        JOptionPane.showMessageDialog(null, scrollPane);
	}
	
	// generates dynamic length blank
	private static String dynamicBlank(int len) {
		
		String space = " ";
		StringBuilder blank = new StringBuilder();		
		for (int i = 0; i < len; i++) {
			blank.append(space);
		}
		return blank.toString();
	}
	
	// processes commands to choose one genre to view sorted movie list
	private void processCMDs() {
		
		if (optionInput.equals("1")) {			
			setSrtdMovieListByGenre(getUnsrtdMovieListByGenre("Adventure"));
			showMoviesByGenreUI();
			//manualTestPrint(srtdMovieListByGenre); // !<- manual test for checking sorted movie list!
			
		} else if (optionInput.equals("2")) {			
			setSrtdMovieListByGenre(getUnsrtdMovieListByGenre("Drama"));
			showMoviesByGenreUI();
			//manualTestPrint(srtdMovieListByGenre); // !<- manual test for checking sorted movie list!
			
		} else if (optionInput.equals("3")) {			
			setSrtdMovieListByGenre(getUnsrtdMovieListByGenre("Fantasy"));
			showMoviesByGenreUI();
			//manualTestPrint(srtdMovieListByGenre); // !<- manual test for checking sorted movie list!
			
		} else if (optionInput.equals("4")) {			
			setSrtdMovieListByGenre(getUnsrtdMovieListByGenre("Romance"));
			showMoviesByGenreUI();
			//manualTestPrint(srtdMovieListByGenre); // !<- manual test for checking sorted movie list!
			
		} else if (optionInput.equals("5")) {			
			setSrtdMovieListByGenre(getUnsrtdMovieListByGenre("Sci Fi"));
			showMoviesByGenreUI();
			//manualTestPrint(srtdMovieListByGenre); // !<- manual test for checking sorted movie list!
			
		} else if (optionInput.equals("6")) {			
			setSrtdMovieListByGenre(getUnsrtdMovieListByGenre("Thriller"));
			showMoviesByGenreUI();
			//manualTestPrint(srtdMovieListByGenre); // !<- manual test for checking sorted movie list!
			
		} else if (optionInput.equals("7")) {			
			setSrtdMovieListByGenre(getUnsrtdMovieListByGenre("War"));
			showMoviesByGenreUI();
			//manualTestPrint(srtdMovieListByGenre); // !<- manual test for checking sorted movie list!
		}
	}
	
	// handles canceling or invalid input
	private static void showMsgDialog(String type) {
			
		if (type.equals("cancelled")) {
			JOptionPane.showMessageDialog(null, "User cancelled, program ends.");
		} else if (type.equals("empty")) {
			JOptionPane.showMessageDialog(null, "No empty input! Please choose one of listed options.");
		} else if (type.equals("invalid")) {
			JOptionPane.showMessageDialog(null, "Invalid input! Please try again.");
		}
	}
	
	// initializes main user interface, providing options to view sorted movie list by chosen genre
	public void initMainUI() {
		
		movie.prcsInFileToStdbyLines();
		movie.setDtrName(movie.stdbyLines.get(0));
		movie.setCprName(movie.stdbyLines.get(1));
		
		String illegalCMDs = "890";
		isValid = false;
		do {
			optionInput = JOptionPane.showInputDialog(null, 
				"Director/Composer Movies" + "\n\n"
				+ "Director: " + movie.getDtrName() + "\n"
				+ "Composer: " + movie.getCprName() + "\n\n"
				+ "Which genre would you like:\n\n"
				+ "1. Adventure\n"
				+ "2. Drama\n"
				+ "3. Fantasy\n"
				+ "4. Romance\n"
				+ "5. Sci Fi\n"
				+ "6. Thriller\n"
				+ "7. War\n\n"
				+ "Your choice: ");
			
			if (optionInput == null) {
				showMsgDialog("cancelled");
				System.exit(0);
			} else if (optionInput.length() == 0) {		
				showMsgDialog("empty");
			} else if (optionInput.length() > 1) {
				showMsgDialog("invalid");
			} else if (illegalCMDs.contains(optionInput) || !Character.isDigit(optionInput.charAt(0))) {
				showMsgDialog("invalid");
			} else {
				this.processCMDs();
			}
		} while(!isValid);
	}
	
	/** main program entrance! */
	public static void main(String[] args) {
		
		ShowSortedMovieInfoByGenre show = new ShowSortedMovieInfoByGenre("MovieListing.txt");
		show.initMainUI();
	}

}
