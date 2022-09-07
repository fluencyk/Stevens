/**
School: Stevens Institute of Technology
Topic: Practice of Chapter 1 and 2
* * *
Implemented: 06/09/2022
Refactor: 
Coder Name: Yujun Kong
Enrolled Class: CS-501_WS
Description: To calculate the cost expense of a meal delivery service and show up the invoice to the customer.
*/

package Project_01;

import javax.swing.*;

public class Invoice<E> {
	
	private String input;
	
	private static String msgCancel;
	private static String msgEmpty;
	private static String msgInvalid;
	private static String msgExceeded;
	private static String msgTipLimit;
	
	private static String customerName;
		
	private double subtotalAmount;
		
	private double taxRate;
	private double deliveryRate;
	
	public int minTipRate;
	public int maxTipRate;
	public int maxSubtotal;
	
	private double givenTipRate;
		
	private double taxCharge;
	private double deliveryCharge;
	private double tipAmount;	
	private double grandTotal;
	
	private static String subFee = "Subtotal = $";
	private static String taxFee = "Tax =";
	private static String delFee = "Delivery fee =";
	private static String tipFee = "Tip amount =";
	private static String dueFee = "Total Due = $";
	
	/** base constructor */
	public Invoice() {
		
		this.taxRate = 0.025;
		this.deliveryRate = 0.050;
		
		this.minTipRate = 0;
		this.maxTipRate = 1000;
		this.maxSubtotal = 10000;
		
		setMsg();
	}
	
	/** overloaded constructor with arguments */
	public Invoice(double taxRate, double deliveryRate, int minTipRate, int maxTipRate, int maxSubtotal) {
		
		this.taxRate = taxRate;
		this.deliveryRate = deliveryRate;
		
		this.minTipRate = minTipRate;
		this.maxTipRate = maxTipRate;
		this.maxSubtotal = maxSubtotal;
		
		setMsg();
	}
	
	// setter of messages
	private void setMsg() {
		
		msgCancel = "Operator cancelled, invoice program quits.";
		msgEmpty = "Input cannot be empty! Try again please.";
		msgInvalid = "Input must be positive number! Try again please.";
		msgExceeded = "Subtotal amount exceeds! Try again please.";
		msgTipLimit = "Invalid Tip Amount!" +"\n\n" + "Minimum Tip Rate: 15%\n" + "Maximum Tip Rate: 100%\n\n" + "Try again please.";
	}
	
	// get sequential inputs from the user
	public void getInput(String dialog) {
		
		if (dialog == "name") {
			do {
				this.input = JOptionPane.showInputDialog(null, "Welcome to the Delivery Calculator" + "\n\n" + "Enter Your Name:");
				if (this.isNull()) {
					inputException("cancel");
				}
				if (this.isEmpty()) {
					inputException("empty");
				}
			} while (this.isEmpty());
			
			customerName = this.input;
		}
		
		if (dialog == "subtotal") {
			do {
				this.input = JOptionPane.showInputDialog(null, "Hello! " + customerName + "\n\n" + "Enter the subtotal amount: $");
				if (this.isNull()) {
					inputException("cancel");
				}
				if (this.isEmpty()) {
					inputException("empty");
				}
				if (!this.isValid()) {
					inputException("invalid");
					this.getInput("subtotal");
				}				
			} while (this.isEmpty());
			
			this.subtotalAmount = Double.parseDouble(this.input);
			if (this.isExceeded()) {
				inputException("exceeded");
				this.getInput("subtotal");
			}
		}
		
		if (dialog == "tip") {
			do {
				this.input = JOptionPane.showInputDialog(null, "Suggested Tip Amounts:" + "\n\n"
				+ "15% = "+ String.format("%.2f", this.subtotalAmount * 0.15) + "\n"
				+ "20% = "+ String.format("%.2f", this.subtotalAmount * 0.20) + "\n"
				+ "25% = "+ String.format("%.2f", this.subtotalAmount * 0.25) + "\n\n"
				+ "Enter the tip %:");
				if (this.isNull()) {
					inputException("cancel");
				}
				if (this.isEmpty()) {
					inputException("empty");
				}
				if (!this.isTipCorrect()) {
					inputException("wrong_tip");
					this.getInput("tip");
				}				
			} while (this.isEmpty());
			
			this.givenTipRate = Double.parseDouble(this.input);
		}
	}
	
	// show up messages of invalid inputs
	private static void inputException(String ex) {
		
		if (ex == "cancel") {
			JOptionPane.showMessageDialog(null, msgCancel);
			System.exit(0);
		} else if (ex == "empty") {
			JOptionPane.showMessageDialog(null, msgEmpty);
		} else if (ex == "invalid") {
			JOptionPane.showMessageDialog(null, msgInvalid);
		} else if (ex == "exceeded") {
			JOptionPane.showMessageDialog(null, msgExceeded);
		} else if (ex == "wrong_tip") {
			JOptionPane.showMessageDialog(null, msgTipLimit);
		}
	}
	
	// determine if the user cancels the program
	private boolean isNull() {
		
		if (this.input == null) {
			return true;
		}
		return false;
	}
	
	//
	private boolean isEmpty() {
		if (this.input.isEmpty()) {
			return true;
		}
		return false;
	}
		
	// determine if the input is valid for numbers
	private boolean isValid() {
		
		String allNums = ".0123456789";
		char decimalPoint = '.';
		int count = 0;
		
		if (this.input.startsWith("0") || this.input.startsWith("-") || this.input.startsWith(".") || this.input.endsWith(".")) {
			return false;
		}
		
		for(int k = 1; k < this.input.length() - 1; k++) {
			if (this.input.length() >= 3) {
				if (this.input.charAt(k) == decimalPoint) {
					count++;
					if (count > 1) {
						return false;
					}
				}
			}
		}
		
		for (int i = 0; i < this.input.length(); i++) {
			if (!allNums.contains(toString(this.input.charAt(i)))) {
				return false;
			}
		}
		return true;
	}
	
	// determine if the sub-total amount is exceeded
	private boolean isExceeded() {
		
		if (this.subtotalAmount > this.maxSubtotal) {
			return true;
		}
		return false;
	}
	
	// determine if the tip set is okay
	private boolean isTipCorrect() {
		
		String allNums = "0123456789";
		int givenTip = 0;
		char point = '.';
		
		for (int i = 0; i < this.input.length(); i++) {
			if (!allNums.contains(toString(this.input.charAt(i)))) {
				return false;
			} else if (this.input.startsWith("0")) {
				return false;
			} else {
				for (int j = 0; j < this.input.length(); j++) {
					if (this.input.charAt(j) == point) {
						this.input = this.input.substring(0, j);
					}
				}
				givenTip = Integer.parseInt(this.input);
			}
		}
		
		if (givenTip < this.minTipRate || givenTip > this.maxTipRate) {
			return false;
		}
		
		return true;
	}
	
	// calculate the invoice's contents
	private void calculation() {
		
		this.taxCharge = this.subtotalAmount * this.taxRate;
		this.deliveryCharge = this.subtotalAmount * this.deliveryRate;
		this.tipAmount = this.subtotalAmount * (this.givenTipRate * 0.01);
		
		this.grandTotal = this.subtotalAmount + this.taxCharge + this.deliveryCharge + this.tipAmount;
	}
	
	// generate the items in the invoice
	private static String invoiceItems(String head, String tail) {
		
		String currItem = "";
		StringBuilder space = new StringBuilder();
		
		for (int i = 0; i < (25 - head.length() - tail.length()); i++) {
			space.append(" ");
		}
		currItem = head + space + tail;
		return currItem;
	}
	
	// convert anything to string format
	private String toString(Object obj) {
		
		return obj.toString();		
	}
	
	// show up the invoice with all info
	public void showInvoice() {
		
		this.getInput("name");
		this.getInput("subtotal");
		this.getInput("tip");
		this.calculation();
		
		JOptionPane.showMessageDialog(
		
		null, "Your Delivery Cost:" + "\n\n"
		+ invoiceItems(subFee, String.format("%.2f", this.subtotalAmount)) + "\n"
		+ invoiceItems(taxFee, String.format("%.2f", this.taxCharge)) + "\n"
		+ invoiceItems(delFee, String.format("%.2f", this.deliveryCharge)) + "\n"
		+ invoiceItems(tipFee, String.format("%.2f", this.tipAmount)) + "\n"
		+ invoiceItems(dueFee, String.format("%.2f", this.grandTotal)) + "\n"
		
		);
	}
	
	/** initializing the program */
	public static void main(String[] args) {

		Invoice standardMealDeliveryCost = new Invoice(0.065, 0.100, 15, 100, 1000);
		standardMealDeliveryCost.showInvoice();
		
		System.exit(0);
	}

}

/** Program ends. */