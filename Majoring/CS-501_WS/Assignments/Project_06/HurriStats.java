/**
School: Stevens Institute of Technology
Topic: Practice of Chapter 9
* * *
Implemented: 21/11/2022(DD/MM/YYYY)
Coder Name: Yujun Kong
Enrolled Class: CS-501_WS
Description: processing text and fathoming wrapper classes, read input file and write data to different output files
*/

package Project_06;

import java.awt.Font;
import java.io.*;
import java.util.*;
import javax.swing.*;

public class HurriStats {
	
	/** general title */
	private static String generalTitle = "Florida Named Hurricanes 1950 - 2022" + "\n\n";
	
	/** fields of file input and output */
	private static String inFilePath;
	static private String outFilePath;
	
	/** field of handling while loops */
	private static boolean isValid;
	
	/** field of user inputting */
	private static String optionInput;
	
	/** fields of unsorted and sorted list objects */
	private static ArrayList<ArrayList<String>> unsrtdRdyLines;
	private static ArrayList<ArrayList<String>> srtdLines;
	
	/** fields of displaying sorted ascending and descending ordered in dialog panels */
	private static Object[] fmtdAscdgLst;
	private static Object[] fmtdDscdgLst;
	
	/** fields of outputting contents to respective files */
	private static Object[] AscdgSrtdOutputLines;
	private static Object[] DscdgSrtdOutputLines;

	/** default constructor */
	public HurriStats() {
		// TODO
	}
	
	/** currently using constructor */
	public HurriStats(String fileName) {
		
		inFilePath = "src/Project_06/" + fileName;
		getUnsrtdRdyLines();
	}
	
	/** manual testing for checking any list */
	public static void manualTestPrint(ArrayList<ArrayList<String>> lst) {
		
		for (int i = 0; i < lst.size(); i++) {
			System.out.println(lst.get(i));
		}
	}
	
	// generates firm length blank
	private static String firmBlank(int lenVal) {
		
		String space = " ";
		StringBuilder blank = new StringBuilder();
				
		for (int i = 0; i < lenVal; i++) {
			blank.append(space);
		}
		return blank.toString();
	}
	
	// generates dynamic length blank
	private static String dycBlank(int lenVal) {
		
		String space = " ";
		StringBuilder blank = new StringBuilder();
		int len = 0;
		int baseVal = 16
				;
		
		if (lenVal == 0) {
			len = 10;
		} else {
			len = baseVal - lenVal;
		}		
		for (int i = 0; i < len; i++) {
			blank.append(space);
		}
		return blank.toString();
	}
	
	// handles each line from file
	private static ArrayList<String> toUnsrtdRdyLine(String inFileline) {
		
		ArrayList<String> line = new ArrayList<String>();
		
		for (int i = 0; i < inFileline.indexOf(":") + 1; i++) {
			if (Character.isAlphabetic(inFileline.charAt(i))) {
				line.add(String.valueOf((char) inFileline.charAt(i) + 0));
			} else {
				line.add(String.valueOf(inFileline.charAt(i)));
			}
		}
		line.add((String) inFileline.subSequence(inFileline.length() - 10, inFileline.length() - 8));
		line.add("/");
		line.add((String) inFileline.subSequence(inFileline.length() - 7, inFileline.length() - 5));
		line.add("/");
		line.add((String) inFileline.subSequence(inFileline.length() - 4, inFileline.length()));
		line.add((String) inFileline.subSequence(inFileline.length() - 10, inFileline.length() - 8));
		line.add((String) inFileline.subSequence(inFileline.length() - 7, inFileline.length() - 5));
		line.add((String) inFileline.subSequence(inFileline.length() - 4, inFileline.length()));
		
		return line;
	}
	
	// gets sorted output contents to respective files
	private static void getSrtdOutputLines() {
		
		ArrayList<String> stdStrList = new ArrayList<String>();
		ArrayList<String> rvsdStdStrList = new ArrayList<String>();
		
		for(int f = 0; f < srtdLines.size(); f++) {
			StringBuilder lineStr = new StringBuilder();
			StringBuilder headStr = new StringBuilder();
			StringBuilder midStr = new StringBuilder();
			StringBuilder tailStr = new StringBuilder();
			
			for(int g = 0; g < srtdLines.get(f).indexOf(","); g++) {				
				headStr.append((char) Integer.parseInt(srtdLines.get(f).get(g)));
			}			
			midStr.append(srtdLines.get(f).get(srtdLines.get(f).indexOf(",") + 1));
			for(int h = srtdLines.get(f).indexOf(":") + 1; h < srtdLines.get(f).size() - 3; h++) {				
				tailStr.append(srtdLines.get(f).get(h));
			}
			lineStr.append(headStr);
			lineStr.append(", ");
			lineStr.append(midStr);
			lineStr.append(", ");
			lineStr.append(tailStr);
			lineStr.append(" \n");
			stdStrList.add(lineStr.toString().replace("/", "-"));
		}
		
		AscdgSrtdOutputLines = stdStrList.toArray();
		for (int i = stdStrList.size() - 1; i > - 1; i--) {
			rvsdStdStrList.add(stdStrList.get(i));
		}
		DscdgSrtdOutputLines = rvsdStdStrList.toArray();
	}
	
	// gets formatted string array to display in text area of target dialog panel
	private static void getFormattedOrder(){
		
		ArrayList<String> fmtdStrList = new ArrayList<String>();
		ArrayList<String> rvsdFmtdStrList = new ArrayList<String>();
		
		for(int f = 0; f < srtdLines.size(); f++) {
			StringBuilder lineStr = new StringBuilder();
			StringBuilder headStr = new StringBuilder();
			StringBuilder midStr = new StringBuilder();
			StringBuilder tailStr = new StringBuilder();
			
			for(int g = 0; g < srtdLines.get(f).indexOf(","); g++) {				
				headStr.append((char) Integer.parseInt(srtdLines.get(f).get(g)));
			}			
			midStr.append(srtdLines.get(f).get(srtdLines.get(f).indexOf(",") + 1));
			for(int h = srtdLines.get(f).indexOf(":") + 1; h < srtdLines.get(f).size() - 3; h++) {				
				tailStr.append(srtdLines.get(f).get(h));
			}
			lineStr.append(" " + headStr);
			lineStr.append(dycBlank(headStr.length()));
			lineStr.append(midStr);
			lineStr.append(dycBlank(0));
			lineStr.append(tailStr);
			lineStr.append(" \n");
			fmtdStrList.add(lineStr.toString().replace("/", "-"));
		}
		
		fmtdAscdgLst = fmtdStrList.toArray();
		for (int i = fmtdStrList.size() - 1; i > - 1; i--) {
			rvsdFmtdStrList.add(fmtdStrList.get(i));
		}
		fmtdDscdgLst = rvsdFmtdStrList.toArray();
	}
	
	// identifies shortest name then determines if capable of swapping to sort
	private static boolean isSwapApplicable(ArrayList<String> listOne, ArrayList<String> listTwo) {
		
		int min = 0;		
		if (listOne.size() == listTwo.size()) {
			min = listOne.size();
		} else if (listOne.size() < listTwo.size()) {
			min = listOne.size();
		} else if (listOne.size() > listTwo.size()) {
			min = listTwo.size();
		}
		
		int i = 0;
		for (int j = 0; j < min; j++) {
			if(Integer.parseInt(listOne.get(i)) == Integer.parseInt(listTwo.get(i))) {
				i++;
			} else if (Integer.parseInt(listOne.get(i)) > Integer.parseInt(listTwo.get(i))) {
				return true;
			} else {
				return false;
			}
		}
		return false;
	}
	
	// gets sorted lines by processing readily unsorted lines from input file
	private static void getSrtdLines(String sortType) {
		
		ArrayList<ArrayList<String>> cmprAL = new ArrayList<ArrayList<String>>();
		
		for (int i = 0; i < unsrtdRdyLines.size(); i++) {									
			ArrayList<String> slcdAL = new ArrayList<String>();
			
			if (sortType.equals("name")) {
				for(int a = 0; a < unsrtdRdyLines.get(i).indexOf(","); a++) {
					slcdAL.add(unsrtdRdyLines.get(i).get(a));
				}
			}
			if (sortType.equals("category")) {
				slcdAL.add(unsrtdRdyLines.get(i).get(unsrtdRdyLines.get(i).indexOf(",") + 1));
			}
			if (sortType.equals("year")) {
				for(int b = unsrtdRdyLines.get(i).size() - 4; b < unsrtdRdyLines.get(i).size() - 1; b++) {
					slcdAL.add(unsrtdRdyLines.get(i).get(b));
				}
			}
			if (sortType.equals("month")) {
				for(int c = unsrtdRdyLines.get(i).size() - 3; c < unsrtdRdyLines.get(i).size(); c++) {
					slcdAL.add(unsrtdRdyLines.get(i).get(c));
				}
			}
			cmprAL.add(slcdAL);
		}
		
		ArrayList<String> tempAL = new ArrayList<String>();		
		for (int i = 0; i < cmprAL.size(); i++) {
			
			for (int j = i + 1; j < cmprAL.size(); j++) {				
				if (!isSwapApplicable(cmprAL.get(i), cmprAL.get(j))) {
					cmprAL.set(i, cmprAL.get(i));
					cmprAL.set(j, cmprAL.get(j));									
				} else if (isSwapApplicable(cmprAL.get(i), cmprAL.get(j))) {
					tempAL = cmprAL.get(j);
					cmprAL.set(j, cmprAL.get(i));
					cmprAL.set(i, tempAL);
					tempAL = unsrtdRdyLines.get(j);
					unsrtdRdyLines.set(j, unsrtdRdyLines.get(i));
					unsrtdRdyLines.set(i, tempAL);
				}
			}			
		}		
		srtdLines = unsrtdRdyLines;
	}
	
	// gets readily unsorted lines from input file
	private static void getUnsrtdRdyLines() {
		
		File inFile = new File(inFilePath);
		ArrayList<ArrayList<String>> inFileLines = new ArrayList<ArrayList<String>>();
		
		try (Scanner in = new Scanner(inFile)) {
			while(in.hasNext()) {
				inFileLines.add(toUnsrtdRdyLine(in.nextLine()));
			}
		} catch (FileNotFoundException e) {
			System.out.println("No such file! Program ends.");
			System.exit(0);
		}
		unsrtdRdyLines = inFileLines;
	}
	
	// shows statistics of aggregated data by storm year
	// command: 8
	private static void showTotalNumStormYr() {
		
		ArrayList<String> yearsStormOccurred = new ArrayList<String>();		
		for (int i = 0; i < unsrtdRdyLines.size(); i++) {
			String tempStr = new String(unsrtdRdyLines.get(i).get(unsrtdRdyLines.get(i).size() - 1));
			yearsStormOccurred.add(tempStr);
		}
		ArrayList<String> yearsStormRelated = new ArrayList<String>();
		for (String j: yearsStormOccurred) {
			if (!yearsStormRelated.contains(j)) {
				yearsStormRelated.add(j);
			}
		}
		
		ArrayList<ArrayList<Integer>> unsrtdYearsWithStormTimes = new ArrayList<ArrayList<Integer>>();
		for (int a = 0; a < yearsStormRelated.size(); a++) {
			ArrayList<Integer> tempUnit = new ArrayList<Integer>();
			int times = 0;
			for (int b = 0; b < yearsStormOccurred.size(); b++) {
				if (yearsStormOccurred.get(b).equals(yearsStormRelated.get(a))) {
					times++;
				}				
			}
			tempUnit.add(Integer.parseInt(yearsStormRelated.get(a)));
			tempUnit.add(times);
			unsrtdYearsWithStormTimes.add(tempUnit);
		}
		
		ArrayList<Integer> tempAL = new ArrayList<Integer>();
		for (int c = 0; c < unsrtdYearsWithStormTimes.size(); c++) {
			for (int d = c + 1; d < unsrtdYearsWithStormTimes.size(); d++) {
				if (unsrtdYearsWithStormTimes.get(c).get(0) > unsrtdYearsWithStormTimes.get(d).get(0)) {
					tempAL = unsrtdYearsWithStormTimes.get(d);
					unsrtdYearsWithStormTimes.set(d, unsrtdYearsWithStormTimes.get(c));
					unsrtdYearsWithStormTimes.set(c, tempAL);
				}
			}
		}
		
		ArrayList<ArrayList<Integer>> srtdYearsWithStormTimes = unsrtdYearsWithStormTimes;
		String resultMsg = "";
		for (int e = 0; e < srtdYearsWithStormTimes.size(); e++) {
			String tempStr = srtdYearsWithStormTimes.get(e).get(0).toString()
			+ firmBlank(21)
			+ srtdYearsWithStormTimes.get(e).get(1).toString() + "\n";
			resultMsg = resultMsg + tempStr;
		}
		
		JOptionPane.showMessageDialog(null, 
				generalTitle
				+ "Aggregate Totals by Year" + "\n\n"
				+ "Year" + firmBlank(6) + "Number of Storms" + "\n"
				+ resultMsg);
	}
	
	// shows statistics of aggregated data by storm category
	// command: 7
	private static void showTotalNumStormCtgy() {
		
		ArrayList<String> allCtgyNums = new ArrayList<String>();
		for (int i = 0; i < unsrtdRdyLines.size(); i++) {
			allCtgyNums.add(unsrtdRdyLines.get(i).get(unsrtdRdyLines.get(i).indexOf(",") + 1));
		}		
		ArrayList<String> distinctAllCtgyNums = new ArrayList<String>();
		for (String j: allCtgyNums) {
			if (!distinctAllCtgyNums.contains(j)) {
				distinctAllCtgyNums.add(j);
			}
		}
		
		ArrayList<ArrayList<Integer>> unsrtdNumsOfCtgyAndStorm = new ArrayList<ArrayList<Integer>>();
		for (int a = 0; a < distinctAllCtgyNums.size(); a++) {
			ArrayList<Integer> tempUnit = new ArrayList<Integer>();
			int count = 0;
			for (int b = 0; b < allCtgyNums.size(); b++) {
				if (allCtgyNums.get(b).equals(distinctAllCtgyNums.get(a))) {
					count++;
				}
			}
			tempUnit.add(Integer.parseInt(distinctAllCtgyNums.get(a)));
			tempUnit.add(count);
			unsrtdNumsOfCtgyAndStorm.add(tempUnit);
		}
		
		ArrayList<Integer> tempAL = new ArrayList<Integer>();
		for (int c = 0; c < unsrtdNumsOfCtgyAndStorm.size(); c++) {
			for (int d = c + 1; d < unsrtdNumsOfCtgyAndStorm.size(); d++) {
				if (unsrtdNumsOfCtgyAndStorm.get(c).get(0) < unsrtdNumsOfCtgyAndStorm.get(d).get(0)) {
					tempAL = unsrtdNumsOfCtgyAndStorm.get(d);
					unsrtdNumsOfCtgyAndStorm.set(d, unsrtdNumsOfCtgyAndStorm.get(c));
					unsrtdNumsOfCtgyAndStorm.set(c, tempAL);
				}
			}
		}
		
		ArrayList<ArrayList<Integer>> srtdNumsOfCtgyAndStorm = unsrtdNumsOfCtgyAndStorm;
		String resultMsg = "";
		for (int e = 0; e < srtdNumsOfCtgyAndStorm.size(); e++) {
			String tempStr = "Total category " + srtdNumsOfCtgyAndStorm.get(e).get(0).toString()
			+ " hurricanes: " + srtdNumsOfCtgyAndStorm.get(e).get(1).toString() + "\n";
			resultMsg = resultMsg + tempStr;
		}
		
		JOptionPane.showMessageDialog(null, 
				generalTitle
				+ "Aggregate Totals by Category (Saffir-Simpson scale)" + "\n\n"
				+ "Total Number of Named Hurricanes = " + String.valueOf(unsrtdRdyLines.size()) + "\n\n"
				+ resultMsg);
	}
	
	// shows statistics of most active years occurred hurricanes
	// command: 6
	private static void showMostActHurriYr() {
		
		ArrayList<String> yearsStormOccurred = new ArrayList<String>();		
		for (int i = 0; i < unsrtdRdyLines.size(); i++) {
			String tempStr = new String(unsrtdRdyLines.get(i).get(unsrtdRdyLines.get(i).size() - 1));
			yearsStormOccurred.add(tempStr);
		}
		ArrayList<String> yearsStormRelated = new ArrayList<String>();
		for (String j: yearsStormOccurred) {
			if (!yearsStormRelated.contains(j)) {
				yearsStormRelated.add(j);
			}
		}
		
		ArrayList<ArrayList<Integer>> yearsWithActiveTimes = new ArrayList<ArrayList<Integer>>();
		for (int a = 0; a < yearsStormRelated.size(); a++) {
			ArrayList<Integer> tempUnit = new ArrayList<Integer>();
			int times = 0;
			for (int b = 0; b < yearsStormOccurred.size(); b++) {
				if (yearsStormOccurred.get(b).equals(yearsStormRelated.get(a))) {
					times++;
				}				
			}
			tempUnit.add(Integer.parseInt(yearsStormRelated.get(a)));
			tempUnit.add(times);
			yearsWithActiveTimes.add(tempUnit);
		}
		
		ArrayList<Integer> tempAL = new ArrayList<Integer>();
		for (int c = 0; c < yearsWithActiveTimes.size(); c++) {			
			for (int d = c + 1; d < yearsWithActiveTimes.size(); d++) {
				if (yearsWithActiveTimes.get(c).get(1) < yearsWithActiveTimes.get(d).get(1)) {
					tempAL = yearsWithActiveTimes.get(d);
					yearsWithActiveTimes.set(d, yearsWithActiveTimes.get(c));
					yearsWithActiveTimes.set(c, tempAL);
				}
			}
		}
		
		String resultMsg = "";
		String yearsCombination = "";
		String yearLabel = yearsWithActiveTimes.get(0).get(0).toString();		
		ArrayList<ArrayList<Integer>> mostActYears = new ArrayList<ArrayList<Integer>>();
		mostActYears.add(yearsWithActiveTimes.get(0));
		for (int e = 1; e < yearsWithActiveTimes.size(); e++) {
			if (yearsWithActiveTimes.get(e).get(1) != yearsWithActiveTimes.get(0).get(1)) {
				yearsCombination = yearLabel;
			} else if (yearsWithActiveTimes.get(e).get(1) == yearsWithActiveTimes.get(0).get(1)) {
				mostActYears.add(yearsWithActiveTimes.get(e));
			}
		}
		if (mostActYears.size() == 1) {
			resultMsg = "Most active storm year is " + yearsCombination + " having " 
						+ mostActYears.get(0).get(1).toString() + " named storms";
		} else if (mostActYears.size() == 2) {
			yearsCombination = mostActYears.get(0).get(0).toString() + " and " + mostActYears.get(1).get(0).toString();
			resultMsg = "Most active storm year is tied with " + yearsCombination + " each having " 
						+ mostActYears.get(0).get(1).toString() + " named storms";
		} else if (mostActYears.size() > 2) {
			for (int f = 0; f < mostActYears.size(); f++) {
				yearsCombination = mostActYears.get(f).get(0).toString() + ", ";
			}
			resultMsg = "Most active storm year is tied with " + yearsCombination + " each having " 
						+ mostActYears.get(0).get(1).toString() + " named storms";
		}
		
		JOptionPane.showMessageDialog(null, 
				generalTitle
				+ "Most Active Storm Year" + "\n\n"
				+ resultMsg);
	}
	
	// shows average storm category
	// command: 5
	private static void showAvgStormCtgy() {
		
		double avgStormCtgyNum;
		double SumOfCtgyNums = 0;
		getUnsrtdRdyLines();		
		for (int i = 0; i < unsrtdRdyLines.size(); i++) {
			SumOfCtgyNums = SumOfCtgyNums + Integer.parseInt(unsrtdRdyLines.get(i).get(unsrtdRdyLines.get(i).indexOf(",") + 1));
		}
		avgStormCtgyNum = SumOfCtgyNums / unsrtdRdyLines.size();
		
		JOptionPane.showMessageDialog(null, 
			generalTitle
			+ "Average Storm Category by Saffir-Simpson Scale" + "\n\n"
			+ "Average Storm Category is " + String.format("%.1f", avgStormCtgyNum));
	}
	
	// shows sorted result of each sorting functionality, outputs sorted contents to respective files
	// commands: 1 ~ 4
	public static void showMsgSrtdOption(String option, String orderDirection) {
		
		String msgHeader = new String(
	        " " + generalTitle +
	        " Sort by Hurricane " + option + " in " + orderDirection + " Order " + "\n\n" +
	        " Name        Category       Date" + "\n");		
		StringBuilder srtdContent = new StringBuilder();
		Object[] srtdLst = null;
		
		if (option.equals("Name")) {
			getSrtdLines("name");
			getFormattedOrder();
			getSrtdOutputLines();
			outFilePath = "src/Project_06/SortByNameKong.txt";
		} else if (option.equals("Category")) {
			getSrtdLines("category");
			getFormattedOrder();
			getSrtdOutputLines();
			outFilePath = "src/Project_06/SortByCategoryKong.txt";
		} else if (option.equals("Year")) {
			getSrtdLines("year");
			getFormattedOrder();
			getSrtdOutputLines();
			outFilePath = "src/Project_06/SortByYearKong.txt";
		} else if (option.equals("Month")) {
			getSrtdLines("month");
			getFormattedOrder();
			getSrtdOutputLines();
			outFilePath = "src/Project_06/SortByMonthKong.txt";
		}
		
		File outFile = new File(outFilePath);
		try (PrintWriter out = new PrintWriter(outFile)) {
			out.print("- ASCENDING ORDER -" + "\n" + "----- ----- ----- ----- -----" + "\n" + "NAME, CATEGORY, DATE" + "\n");
			for (int i = 0; i < AscdgSrtdOutputLines.length; i++) {
				out.print(AscdgSrtdOutputLines[i]);
			}
			out.print("\n" + "- DESCENDING ORDER -" + "\n" + "----- ----- ----- ----- -----" + "\n" + "NAME, CATEGORY, DATE" + "\n");
			for (int j = 0; j < DscdgSrtdOutputLines.length; j++) {
				out.print(DscdgSrtdOutputLines[j]);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			JOptionPane.showMessageDialog(null, "File Output Error! Program ends.");
			System.exit(0);
		}
		
		if (orderDirection.equals("Ascending")) {
			srtdLst = fmtdAscdgLst;
		} else if (orderDirection.equals("Descending")) {
			srtdLst = fmtdDscdgLst;
		}
		
		for (int j = 0; j < srtdLst.length; j++) {
			srtdContent.append(srtdLst[j].toString());
		}
		
		JTextArea textArea = new JTextArea(msgHeader + srtdContent.toString(), 15, 50);		
		textArea.setFont(new java.awt.Font("monospaced", Font.PLAIN, 14));         
        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        scrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED);
		
        JOptionPane.showMessageDialog(null, scrollPane);
	}
	
	// shows interval interface of 4 sorting functionalities
	public void showSortOptions(String sortOption) {
		
		do {
			optionInput = JOptionPane.showInputDialog(null, 
				"Florida Named Hurricanes 1950 - 2022" + "\n\n" +
				"Sort by Hurricane " + sortOption + "\n\n" +
				"Press 1 for Ascending Order" + "\n" +
				"Press 2 for Descending Order" + "\n\n"
			);
			if (optionInput == null) {
				this.showDashboard();
			} else if (optionInput.length() == 0) {		
				showMsgDialog("empty");
			} else if (!optionInput.equals("1") && !optionInput.equals("2")) {
				showMsgDialog("invalid");
			}
			
			if (sortOption.equals("Name")) {
				if (optionInput.equals("1")) {				
					showMsgSrtdOption("Name", "Ascending");
				} else if (optionInput.equals("2")) {
					showMsgSrtdOption("Name", "Descending");
				}
			} else if (sortOption.equals("Category")) {
				if (optionInput.equals("1")) {				
					showMsgSrtdOption("Category", "Ascending");
				} else if (optionInput.equals("2")) {
					showMsgSrtdOption("Category", "Descending");
				}
			} else if (sortOption.equals("Year")) {
				if (optionInput.equals("1")) {				
					showMsgSrtdOption("Year", "Ascending");
				} else if (optionInput.equals("2")) {
					showMsgSrtdOption("Year", "Descending");
				}
			} else if (sortOption.equals("Month")) {
				if (optionInput.equals("1")) {				
					showMsgSrtdOption("Month", "Ascending");
				} else if (optionInput.equals("2")) {
					showMsgSrtdOption("Month", "Descending");
				}
			}
		} while(!isValid);
	}
	
	// processes commands for 9 contained functionalities
	private void processCMDs() {
		
		if (optionInput.equals("1")) {
			this.showSortOptions("Name");
		} else if (optionInput.equals("2")) {
			this.showSortOptions("Category");
		} else if (optionInput.equals("3")) {
			this.showSortOptions("Year");
		} else if (optionInput.equals("4")) {
			this.showSortOptions("Month");
		} else if (optionInput.equals("5")) {
			showAvgStormCtgy();
		} else if (optionInput.equals("6")) {
			showMostActHurriYr();
		} else if (optionInput.equals("7")) {
			showTotalNumStormCtgy();
		} else if (optionInput.equals("8")) {
			showTotalNumStormYr();
		} else if (optionInput.equals("9")) {
			JOptionPane.showMessageDialog(null, "Program exited. Thank you!");
			System.exit(0);
		}
	}
	
	// handles canceling or invalid inputting
	private static void showMsgDialog(String type) {
		
		if (type.equals("cancelled")) {
			JOptionPane.showMessageDialog(null, "User cancelled, program ends.");
		} else if (type.equals("empty")) {
			JOptionPane.showMessageDialog(null, "No empty input! Please choose one listed command.");
		} else if (type.equals("invalid")) {
			JOptionPane.showMessageDialog(null, "Invalid input! Please try again.");
		}
	}
	
	// initializes program, shows dash-board contains 9 commands for sorting or statistics
	public void showDashboard() {
		
		isValid = false;
		do {
			optionInput = JOptionPane.showInputDialog(null, 
				"Florida Named Hurricanes 1950 - 2022" + "\n\n"
				+ "Press 1 to Sort by Storm Name" + "\n"
				+ "Press 2 to Sort by Storm Category" + "\n"
				+ "Press 3 to Sort by Storm Year" + "\n"
				+ "Press 4 to Sort by Storm Month" + "\n"
				+ "Press 5 to Display the Average Storm Category" + "\n"
				+ "Press 6 to Display the Most Active Hurricane Year" + "\n"
				+ "Press 7 to Display the Total Number of Storm by Category" + "\n"
				+ "Press 8 to Display the Total Number of Storm by Year" + "\n"
				+ "Press 9 to Exit" + "\n\n\n"
			);			
			if (optionInput == null) {
				showMsgDialog("cancelled");
				System.exit(0);
			} else if (optionInput.length() == 0) {		
				showMsgDialog("empty");
			} else if (optionInput.length() > 1) {
				showMsgDialog("invalid");
			} else if (optionInput.equals("0") || !Character.isDigit(optionInput.charAt(0))) {
				showMsgDialog("invalid");
			} else {
				this.processCMDs();
			}
		} while(!isValid);
		
	}
	
	/** program entrance */
	public static void main(String[] args) {
		
		HurriStats hs = new HurriStats("NamedFloridaHurricanes.txt");
		/** manual testing
		//manualTestPrint(unsrtdRdyLines);
		//System.out.println("----- ----- ----- ----- ----- ----- ----- ----- ----- -----");
		*/
		hs.showDashboard();
	}

}
/** end of programming */
