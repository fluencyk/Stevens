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

import java.util.*;

public class Analysis {
	
	private static ArrayList<ArrayList<Integer>> asciiList;
	private static ArrayList<StringBuffer> srtdWdsList;
	private static ArrayList<String> flzdList;
	
	/** default constructor */
	public Analysis() {
		
	}
	
	// getter method
	public static ArrayList<ArrayList<Integer>> getAsciiList(){
		
		return asciiList;
	}
	
	// getter method
	public static ArrayList<StringBuffer> getWdsList(){
		
		return srtdWdsList;
	}
	
	// getter method
	public static ArrayList<String> getFlzdList(){
		
		return flzdList;
	}
	
	// converting to word
	private static char toAscii(int num) {
		
		return (char)num;
	}
	
	// turning back sorted numbers to words
	public static ArrayList<StringBuffer> toWdsList(){
		
		ArrayList<ArrayList<Integer>> numsLst = getAsciiList();
		ArrayList<StringBuffer> wdsLst = new ArrayList<StringBuffer>();		
		
		for (int i = 0; i < numsLst.size(); i++) {
			char[] tmpLst = new char[numsLst.size()];
			StringBuffer tmpStr = new StringBuffer();
			for (int j = 0; j < numsLst.get(i).size(); j++) {
				tmpLst[j] =  toAscii(numsLst.get(i).get(j) + 96);
				tmpStr.append(tmpLst[j]);
			}			
			wdsLst.add(tmpStr);	
		}		
		return srtdWdsList = wdsLst;
	}
	
	// converting words to ASCII numbers for sorting
	private static ArrayList<Integer> weightWord(String word) {
		
		ArrayList<Integer> wghtdNums = new ArrayList<Integer>();
		for (int i = 0; i < word.length(); i++) {
			int tmpNum = word.charAt(i) - 96;
			wghtdNums.add(tmpNum);
		}		
		return wghtdNums;
	}
	
	// setter method
	public static ArrayList<ArrayList<Integer>> setNumList(String[] words) {
		
		ArrayList<ArrayList<Integer>> numList = new ArrayList<ArrayList<Integer>>();
		for (int i = 0; i < words.length; i++) {
			numList.add(weightWord(words[i]));
		}		
		return numList;
	}
	
	// setter method
	public static ArrayList<ArrayList<Integer>> sortWdsList(ArrayList<ArrayList<Integer>> arrLst){
		
		ArrayList<Integer> tempAL = new ArrayList<Integer>();
		
		for (int i = 0; i < arrLst.size(); i++) {
			
			for (int j = i + 1; j < arrLst.size(); j++) {
			
				int k = 0;
				if (arrLst.get(i).get(k) == arrLst.get(j).get(k)) {
					arrLst.set(i, arrLst.get(i));
					arrLst.set(j, arrLst.get(j));
					k++;
				}
				if (arrLst.get(i).get(k) > arrLst.get(j).get(k)) {
					tempAL = arrLst.get(j);
					arrLst.set(j, arrLst.get(i));
					arrLst.set(i, tempAL);					
				}
			}
		}		
		return asciiList = arrLst;
	}
	
	// determine if string is same after reversed
	private static boolean isPalindrome(String str) {
		
		StringBuffer tmpStrBfr = new StringBuffer(str);
		if (str.equals(tmpStrBfr.reverse().toString())) {
			return true;
		} else {
			return false;
		}
	}
	
	// generate dynamic length blank spaces
	private static StringBuilder dycBlank(int lenVal) {
		
		String space = " ";
		StringBuilder blank = new StringBuilder();
		int len = 0;
		int baseVal = 12;
		
		if (lenVal == 0) {
			len = 6;
		} else {
			len = baseVal - lenVal;
		}		
		for (int i = 0; i < len; i++) {
			blank.append(space);
		}
		return blank;
	}
	
	// finalizing core analyzed content
	public static ArrayList<String> fnlzdList() {
		
		ArrayList<String> fzdLst = new ArrayList<String>();
		ArrayList<StringBuffer> prcsLst = getWdsList();
		
		ArrayList<String> tmpStr = new ArrayList<String>();		
		for (int i = 0; i < prcsLst.size(); i++) {
			tmpStr.add(prcsLst.get(i).toString());
		}				
		ArrayList<String> tmpSet = new ArrayList<>(new LinkedHashSet<>(tmpStr));
					
		for (int i = 0; i < tmpSet.size(); i++) {
			int count = 0;
			for (int j = 0; j < tmpStr.size(); j++) {
				if (tmpStr.get(j).equals(tmpSet.get(i))) {
					count++;
				}
			}
			if (isPalindrome(tmpSet.get(i)) == true) {
				fzdLst.add("   " + tmpSet.get(i) + dycBlank(tmpSet.get(i).length()) + count + dycBlank(0) + "ture");
			} else {
				fzdLst.add("   " + tmpSet.get(i) + dycBlank(tmpSet.get(i).length()) + count + dycBlank(0) + "false");
			}
		}
		return flzdList = fzdLst;
	}
	
	// ! manual test method
	public static void printArrList(ArrayList<StringBuffer> arrLst) {
		
		for (int i = 0; i < arrLst.size(); i++) {
			System.out.println(arrLst.get(i));
		}
	}
	
	/** program entrance, manual testing */
	public static void main(String[] args) { // !<- manual testing case, DO NOT regard this as main program entrance!
		
		InputFile manualTestCase_outAnalyzedResult = new InputFile("inPoem.txt");
		
		sortWdsList(setNumList(manualTestCase_outAnalyzedResult.getWords()));
		toWdsList();
		fnlzdList();
		
		for (int i = 0; i < flzdList.size(); i++) {
			System.out.println(flzdList.get(i));
		}
		
		System.exit(0);
	}
	
} /** end of programming */
