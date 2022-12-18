/**
 * School: Stevens Institute of Technology
 * Topic: Practice of Advanced Programming Techniques in Data Structure and Algorithms
 * * *
 * Implemented: 12/17/2022
 * Coder Name: Yujun Kong
 * Enrolled Class: CS-501_WS
 * Description: ADT, Linked List
 */

package Project_09;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Scanner;

public class StudentByLetterGrade<E> {
	
	/** fields of each node */
	private Node<E> head;
	private Node<E> tail;
	private int size;
	private boolean isNull; /** if current list is empty */
	
	/** default constructor !used */
	public StudentByLetterGrade() {
		
		this.head = null;
		this.tail = null;
		this.size = 0;
	}
	
	/** overload constructor !unused */
	public StudentByLetterGrade(String inputFileName) {
		
		this.getListFromFileInfo(setInFilePath(inputFileName));
	}
	
	// set input file path
	private String setInFilePath(String inputFileName) {
		
		String inFilePath;		
		inFilePath = "src/Project_09/" + inputFileName;
		return inFilePath;
	}
	
	// process input file info to standby object
	private ArrayList<String[]> getListFromFileInfo(String setInputFileName){
		
		ArrayList<String[]> studentGradeList = new ArrayList<String[]>();
		File inFile = new File(setInputFileName);
		try (Scanner in = new Scanner(inFile)) {
			while(in.hasNext()) {
				String[] line = in.nextLine().split(" ");
				studentGradeList.add(line);
			}
		} catch (FileNotFoundException e) {
			System.out.println("No such file - '" + setInputFileName 
					+ "'! Program ends after clicked OK button.");
		}
		System.out.println("Opening file......");
		
		return studentGradeList;		
	}
	
	/** core method, calculate average grade in point to match letter grade */
	private ArrayList<String[]> getAllStudentGrades(ArrayList<String[]> listFromFileInfo) {
		
		ArrayList<String[]> arrListOfStudentIDwithGrade = new ArrayList<String[]>();
		for (int i = 0; i < listFromFileInfo.size(); i++) {
			String[] eachStudentIDwithGrade = new String[2];
			eachStudentIDwithGrade[0] = listFromFileInfo.get(i)[0];
			String strGrade = null;			
			double grade = 0.0;
			
			double pjtPt_01 = Double.parseDouble(listFromFileInfo.get(i)[1]);
			double pjtPt_02 = Double.parseDouble(listFromFileInfo.get(i)[2]);
			double midPt = Double.parseDouble(listFromFileInfo.get(i)[3]);
			double pjtPt_03 = Double.parseDouble(listFromFileInfo.get(i)[4]);
			double pjtPt_04 = Double.parseDouble(listFromFileInfo.get(i)[5]);
			double fnlPt = Double.parseDouble(listFromFileInfo.get(i)[6]);
			
			grade = (pjtPt_01 + pjtPt_02 + pjtPt_03 + pjtPt_04) / 4 * 0.5 + midPt * 0.2 + fnlPt * 0.3;
			strGrade = String.format("%.1f", grade);
			eachStudentIDwithGrade[1] = strGrade;
			
			arrListOfStudentIDwithGrade.add(eachStudentIDwithGrade);
		}
		System.out.println("Processing file......\n");
		
		return arrListOfStudentIDwithGrade;
	}
	
	/** inner class, define node object of linked list */
	private static class Node<E> {
		
		private String[] data;
		@SuppressWarnings("unused")
		private Node<E> prev;
		private Node<E> next;
		
		@SuppressWarnings("unused")
		public Node() {}
		
		public Node(String[] strings) {
			
			this.data = strings;
			this.prev = null;
			this.next = null;
		}
		
	}
	
	/** core method, add current node to end of linked list */
	private void append(String[] strings) {
		
		Node<E> newNode = new Node<E>(strings);
		
		if (size == 0) {
			head = newNode;
			newNode.prev = null;
			newNode.next = null;
		} else if (size == 1) {
			head.next = newNode;
			newNode.prev = head;
			tail = newNode;
			newNode.prev = head;
			newNode.next = null;
		} else if (size > 1) {
			tail.next = newNode;
			newNode.prev = tail;
			tail = newNode;
			newNode.next = null;
		}
		size++;
	}
	
	/** core method, result specific letter grade earned student */
	private void getCurrListOfStudentIDwithGrade() {
		
		String letterGrade = null;
		String[] validLetterGrades = {"A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F", "Q"};
		ArrayList<String[]> arrLstIDwithGrade = 
				this.getAllStudentGrades(getListFromFileInfo(setInFilePath("studentInfoMore.txt")));
		
		Scanner scanner = new Scanner(System.in);
		boolean isValid = false;
		do {
			System.out.print("Letter Grades: 'A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F'"
					+ " | Quit: 'Q'\n"
					+ "Enter the letter grade earned by students to display -> ");
			try {
				letterGrade = scanner.next();
				if (!Arrays.asList(validLetterGrades).contains(letterGrade)) {
					throw new InputMismatchException();
				} else {
					double max = 0;
					double min = 0;
					String LtrGdPtScope = "";
					if (letterGrade.equals("A")) {
						max = 100;
						min = 94;
						LtrGdPtScope = "(94 - 100%):";
					} else if (letterGrade.equals("A-")) {
						max = 93.9;
						min = 90;
						LtrGdPtScope = "(90 - 93.9%):";
					} else if (letterGrade.equals("B+")) {
						max = 89.9;
						min = 87;
						LtrGdPtScope = "(87 - 89.9%):";
					} else if (letterGrade.equals("B")) {
						max = 86.9;
						min = 83;
						LtrGdPtScope = "(83 - 86.9%):";
					} else if (letterGrade.equals("B-")) {
						max = 82.9;
						min = 80;
						LtrGdPtScope = "(80 - 82.9%):";
					} else if (letterGrade.equals("C+")) {
						max = 79.9;
						min = 77;
						LtrGdPtScope = "(77 - 79.9%):";
					} else if (letterGrade.equals("C")) {
						max = 76.9;
						min = 73;
						LtrGdPtScope = "(73 - 76.9%):";
					} else if (letterGrade.equals("C-")) {
						max = 72.9;
						min = 70;
						LtrGdPtScope = "(70 - 72.9%):";
					} else if (letterGrade.equals("D+")) {
						max = 69.9;
						min = 67;
						LtrGdPtScope = "(67 - 69.9%):";
					} else if (letterGrade.equals("D")) {
						max = 66.9;
						min = 63;
						LtrGdPtScope = "(63 - 66.9%):";
					} else if (letterGrade.equals("D-")) {
						max = 62.9;
						min = 60;
						LtrGdPtScope = "(60 - 62.9%):";
					} else if (letterGrade.equals("F")) {
						max = 59.9;
						min = 0;
						LtrGdPtScope = "(0 - 59.9%):";
					} else if (letterGrade.equals("Q")) {
						System.out.println("Program quits, thank you!");
						scanner.close();
						System.exit(0);
					}
										
					for (int j = 0; j < arrLstIDwithGrade.size(); j++) {
						if (Double.parseDouble(arrLstIDwithGrade.get(j)[1]) <= max
							&& Double.parseDouble(arrLstIDwithGrade.get(j)[1]) >= min) {
							
							this.append(arrLstIDwithGrade.get(j));
							isNull = false;
							
						}
					}
					
					String sdtLstHeader = "\nList of students with a " + letterGrade 
							+ " average " + LtrGdPtScope;
					System.out.println(sdtLstHeader + "\n");
					
					if (size == 0) {
						isNull = true;
					} else if (size >= 1) {
						isNull = false;
					}
					
					
					this.printCurrLinkedList();
					System.out.println("\nEnd of results.\n");
					this.clear();
				}
			} catch (InputMismatchException e) {
				System.out.println("Your input " + letterGrade + " is Invalid! Please try again.");
				scanner.nextLine();
			}			
		} while (!isValid);
	}
	
	// empty linked list
	private void clear() {
		
		head = null;
		tail = null;
		size = 0;
	}
	
	// output the result for user
	public void printCurrLinkedList() {
		
		if (isNull) {
			System.out.println("!!! None of the students earned the input letter grade! Please try another.");
		} else {
			Node<?> currNode = this.head;
			for (int i = 0; i < this.size; i++) {
				System.out.println(currNode.data[0] + " " + currNode.data[1]);
				currNode = currNode.next;
			}	
		}
	}
	
	/** main entrance of program */
	public static void main(String[] args) {

		StudentByLetterGrade<?> sblg = new StudentByLetterGrade<Object>();
		
		System.out.println("Welcome to ' Student by Letter Grade '\n");		
		sblg.getCurrListOfStudentIDwithGrade();
		
	}

} /** end of programming */
