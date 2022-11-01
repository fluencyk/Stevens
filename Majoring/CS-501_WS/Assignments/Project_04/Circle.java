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

public class Circle {
	
	private static final double PI = 3.14159;
	private double radius;
	
	public Circle() {
		
		this.radius = 0.0;
	}
	
	public Circle(double inputVal) {
		
		this.setRadiusVal(inputVal);
	}
	
	public void setRadiusVal(double radiusVal) {
		
		this.radius = radiusVal;
	}
	
	public double getRadiusVal() {
		
		return this.radius;
	}
	
	public double computeArea() {
		
		return PI * Math.pow(this.getRadiusVal(), 2);
	}

}