import java.util.ArrayList;
import java.util.List;

/**
 * A simple linked list implementation that stores a list of students and their grades.
 */
public class StudentList {

    /** The head of the linked list. */
    private Node head;

    /** The tail of the linked list. */
    private Node tail;

    /** The number of nodes in the linked list. */
    private int size;

    /**
     * A class representing a node in the linked list.
     */
    private static class Node {
        private Student student;
        private Node next;
    }

    /**
     * Creates a new, empty student list.
     */
    public StudentList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    /**
     * Returns the number of students in the list.
     */
    public int size() {
        return size;
    }

    /**
     * Returns true if the list is empty, false otherwise.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Adds a new student to the end of the list.
     *
     * @param student the student to add
     */
    public void add(Student student) {
        Node newNode = new Node();
        newNode.student = student;
        newNode.next = null;

        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
        size++;
    }

    /**
     * Returns a list of all students in the list.
     */
    public List<Student> getAllStudents() {
        List<Student> students = new ArrayList<>();
        Node current = head;
        while (current != null) {
            students.add(current.student);
            current = current.next;
        }
        return students;
    }

    /**
     * Removes the student with the given ID from the list.
     *
     * @param id the ID of the student to remove
     * @return true if the student was found and removed, false otherwise
     */
    public boolean remove(String id) {
        Node current = head;
        Node prev = null;
        while (current != null) {
            if (current.student.getId().equals(id)) {
                if (prev == null) {
                    head = current.next;
                } else {
                    prev.next = current.next;
                }
                if (current.next == null) {
                    tail = prev;
                }
                size--;
                return true;
            }
            prev = current;
            current = current.next;
        }
        return false;
    }

    /**
     * Returns the student with the given ID, or null if no such student is found.
     *
     * @param id the ID of the student to search for
     */
    public Student get(String id) {
        Node current = head;
        while (current != null) {
            if (current.student.getId().equals(id)) {
                return current.student;
            }
            current = current.next;
        }
        return null;
    }
}

/**
 * A class representing a student and their grades.
 */
public class Student {

    /** The ID of the student. */
    private String id;

    /** The grades of the student. */
    private List<Double> grades;

    /**
     * Creates a new student with the given ID and grades.
     *
     * @param id the ID of the student
     * @param grades the grades of the student
     */
    public Student(String id, List<Double> grades) {
        this.id = id;
        this.grades = grades;
    }

    /**
     * Returns the ID of the student.
     */
    public String getId() {
        return id;
    }

    /**
     * Returns the grades of the student.
     */
    public List<Double> getGrades() {
        return grades;
    }
}
