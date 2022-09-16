/**
School: Stevens Institute of Technology
Topic: Practice of Chapter 3
* * *
Implemented: 11/09/2022
Refactor: 
Coder Name: Yujun Kong
Enrolled Class: CS-501_WS
Description: To write a Java program that uses object-oriented principles introduced in chapter 3.
*/

package Project_02;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Calculator {
	
	private double value;
	private static double tempVal;
	private static double inputVal;
	
	/** default constructor */
	public Calculator() {
		
		this.value = 0.0;
	}
	
	// plus by the parameter
	public void add(double val) {
		
		tempVal = this.value + val;
		this.value = tempVal;
	}
	
	// subtracting by the parameter
	public void substract(double val) {
		
		tempVal = this.value - val;
		this.value = tempVal;
	}
	
	// multiplying by the parameter
	public void multiply(double val) {
		
		tempVal = this.value * val;
		this.value = tempVal;
	}
	
	// dividing by the parameter
	public void divide(double val) {
		
		tempVal = this.value / val;
		this.value = tempVal;
	}
	
	// reset the class' member field to the value of 0.0
	public void clear() {
		
		this.value = 0.0;
	}
	
	// return the class' member field of 'value'
	public double getValue() {
		
		return this.value;
	}
	
	// convert the given object to string format
	public String toString(Object obj) { /** this method is just for precautions */
		
		return obj.toString();
	}
	
	// get the user's input with the validation
	public void input(String numWhich) {
		
		boolean inputValid = false;
		double number = 0.0;
		Scanner input = new Scanner(System.in);
		
		do {
			if (numWhich == "firstNum") {
				System.out.print("Number One: ");
			} else if (numWhich == "secondNum") {
				System.out.print("Number Two: ");
			}
			
			try {
				number = input.nextDouble();
				inputValid = true;				
			} catch (InputMismatchException ex) {
				System.out.println("The input is not a number, please try again!");
				input.nextLine();
			}			
		} while (!inputValid);
		
		inputVal = number;
	}
	
	/** initializing the program */
	public static void main(String[] args) {

		double num1;
		double num2;
		
		System.out.println("---= Welcome to the program of ' Calculator ' =---");
		System.out.println("----- ----- ----- ----- ----- ----- ----- ----- ----- -----");
		System.out.println("Please input two numbers to calculate...");
		
		Calculator myCal = new Calculator();
		
		myCal.input("firstNum");
		num1 = inputVal;
		myCal.input("secondNum");
		num2 = inputVal;
		
		System.out.println("\n" + "The initial member field 'value' is: " + myCal.toString(myCal.getValue()) + "\n");
		
		myCal.add(num1);
		System.out.println("Adding...(" + String.format("%.1f", num1) + ")");
		System.out.printf("The current member field 'value' is: %.1f" + "\n\n", myCal.getValue());
				
		myCal.multiply(3);
		System.out.println("Multiplying...(" + "3)");
		System.out.printf("The current member field 'value' is: %.1f" + "\n\n", myCal.getValue());
		
		myCal.substract(num2);
		System.out.println("Substracting...(" + String.format("%.1f", num2) + ")");
		System.out.printf("The current member field 'value' is: %.1f" + "\n\n", myCal.getValue());
		
		myCal.divide(2);
		System.out.println("Dividing...(" + "2)");
		System.out.printf("The current member field 'value' is: %.1f" + "\n\n", myCal.getValue());
		
		myCal.clear();
		System.out.println("Clearing...");
		System.out.printf("The cleared(reset) member field 'value' is: %.1f" + "\n\n", myCal.getValue());
	}

}

/** Program ends. */