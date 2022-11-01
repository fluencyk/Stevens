/**
School: Stevens Institute of Technology
Topic: Practice of Chapter 6, 7
* * *
Implemented: 15/09/2022
Coder Name: Yujun Kong
Enrolled Class: CS-501_WS
Description: Classes design in coupling, depending, modeling
*/

package Project_04;

import java.util.Scanner;

public class ShapeAreaCalculation {
	
	private static Scanner scanner = new Scanner(System.in);	
	private static String shapeType;
	private static double sizeVal;
	public static String areaVal;
	
	/** default constructor */
	public ShapeAreaCalculation() {
		
	}
		
	// verify if input value valid for double or integer type
	private static boolean isValid(String inputStr) { /** the very critical core for verifications */
		
		String str = inputStr.strip();
		String legalStr = ".0123456789";
		char deciPoint = '.';
		char zero = '0';
		int count = 0;
		
		if (str.charAt(0) == zero && str.charAt(1) != deciPoint) {
			return false;
		}
		
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == deciPoint) {
				count++;
			}
		}
		
		for (int j = 0; j < str.length(); j++) {			
			if (count > 1) {				
				return false;
			} else if (count == 1) {
				if (!legalStr.contains(Character.toString(str.charAt(j)))) {
					return false;
				} else {
					if (str.charAt(0) == deciPoint) {
						str.replaceAll(str, zero + str);
						return true;
					} else if (str.charAt(str.length() - 1) == deciPoint) {
						str.replaceAll(str, str + zero);
						return true;
					}
				}
			} else if (count == 0) {
				if (legalStr.contains(Character.toString(str.charAt(j)))) {					
					return true;
				}
			}
		}
		
		return true;
	}
	
	// hint invalid input
	private static void hintInvalid() {
		
		System.out.print("Invalid input! Try again, please: ");
	}
	
	// convert string to double
	public static double toDouble(String str) {
		
		return Double.parseDouble(str);
	}
	
	// end program
	private static void quitProgram() {
		
		System.out.println("Program quits, thank you!");
		scanner.close();
		System.exit(0);
	}

	/** above're support modules, below're process logic flows */
	
	// confirm shape type as condition of process
	private static void defShape(String shapeName) {
		
		System.out.println("You selected a " + shapeName + " to calculate the area...");
		shapeType = shapeName;
	}
	
	// menu to choose shape
	private static String optShape() {
		
		System.out.print("Type one command c, r, t to choose a shape to calculate the area, or type q to quit the program."
						+ "\n" + "'c' for Circle, 'r' for Rectangle, 't' for Triangle, or 'q' for Quit."
						+ "\n" + ">> COMMAND: ");
		String cmd;
		do {
			cmd = scanner.next();
			if (cmd.equals("c")) {
				defShape("Circle");
				break;
			} else if (cmd.equals("r")) {
				defShape("Rectangle");
				break;
			} else if (cmd.equals("t")) {
				defShape("Triangle");
				break;
			} else if (cmd.equals("q")) {
				quitProgram();
			} else {
				System.out.println("Invalid command! Try again, please." + "\n" + "Type in 'c' for Circle, 'r' for Rectangle, and 't' for Triangle." + "\n");
				continue;
			}
		} while (cmd != null);
		
		return shapeType;		
	}

	// set and convert input as parameter to calculate area  
	public static double setPara(String paraName) {
		
		System.out.print("Please set " + paraName + " as: ");
		String inVal; 
		do {
			inVal = scanner.next();
			if (!isValid(inVal)) {
				hintInvalid();
				continue;
			} else {
				try {
					sizeVal = toDouble(inVal);
					break;
				} catch (java.lang.NumberFormatException ex) {
					hintInvalid();
					scanner.next();
				}
			}
		} while (inVal != null);
		
		return sizeVal;
	}	
	
	// depend on command to calculate respective shape area
	public static String calcuArea(String shapeID) {
		
		if (shapeID.equals("Circle")) {
			Circle myCir = new Circle(setPara("Radius"));			
			areaVal = String.format("%.2f", myCir.computeArea());
		}
		
		if (shapeID.equals("Rectangle")) {
			Rectangle myRect = new Rectangle(setPara("Length"), setPara("Width"));
			areaVal = String.format("%.2f", myRect.computeArea());
		}
		
		if (shapeID.equals("Triangle")) {
			Triangle myTri = new Triangle(setPara("Base"), setPara("Height"));
			areaVal = String.format("%.2f", myTri.computeArea());			
		}
		
		return areaVal;
	}

	// print calculated shape area value
	public static void printArea() {
		
		System.out.println("-> The " + shapeType + "'s Calculated Area is: " + calcuArea(shapeType) + " sq.ft"
				+ "\n-==== ===== ===== ===== ===== ===== ===== ===== ===== ====-");
	}
	
	// clear member value
	public static void clearVals(String shapeName) {
		
		if (shapeName.equals("Circle")) {
			Circle cir = new Circle();			
			System.out.println("-> Values of " + shapeType + "'s member have been cleared as " 
								+ "Radius: "+cir.getRadiusVal()
								+ "\n----- ----- ----- ----- ----- ----- ----- ----- ----- -----");
		} else if (shapeName.equals("Rectangle")) {
			Rectangle rec = new Rectangle();
			System.out.println("-> The Values of " + shapeType + "'s member have been cleared as " 
								+ "Length: "+rec.getLength() + ", " + "Width: "+rec.getWidth()
								+ "\n----- ----- ----- ----- ----- ----- ----- ----- ----- -----");
		} else if (shapeName.equals("Triangle")) {
			Triangle tri = new Triangle();
			System.out.println("-> Values of " + shapeType + "'s member have been cleared as " 
								+ "Base: "+tri.getBase() + ", " + "Height: "+tri.getHeight()
								+ "\n----- ----- ----- ----- ----- ----- ----- ----- ----- -----");
		}
		
		shapeType = "";
		sizeVal = 0.0;
		areaVal = "";
	}
	
	/** be equal to main()'s processing feature, be avoid to overwhelming complexity in program structure*/
	public void process() {
		
		optShape();
		if (shapeType.equals("Circle")) {
			printArea();
			clearVals(shapeType);
		}
		
		if (shapeType.equals("Rectangle")) {
			printArea();
			clearVals(shapeType);
		}
		
		if (shapeType.equals("Triangle")) {
			printArea();
			clearVals(shapeType);
		}

		process();
	}
	
	/** initializing program */
	public static void main(String[] args) {
		
		ShapeAreaCalculation mySac = new ShapeAreaCalculation();
		mySac.process();
	}

}

/** Program ends. */