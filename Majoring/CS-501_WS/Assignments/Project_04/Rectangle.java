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

public class Rectangle {

	private double length;
	private double width;
	
	public Rectangle() {
		
		this.length = 0.0;
		this.width = 0.0;
	}
	
	public Rectangle(double lenVal, double widVal) {
		
		this.setRadiusVal(lenVal, widVal);
	}
	
	public void setRadiusVal(double len, double wid) {
		
		this.length = len;
		this.width = wid;
	}
	
	public double getLength() {
		
		return this.length;
	}
	
	public double getWidth() {
		
		return this.width;
	}
	
	public double computeArea() {
		
		return this.getLength() * this.getWidth();
	}

}