package 해시;

import java.util.HashMap;
import java.util.Scanner;

public class marathon {

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		
		Scanner input = new Scanner(System.in);
		
		String line1 = input.nextLine();
		String line2 = input.nextLine();
		
		String participant[] = line1.split(" ");
		String completion[] = line2.split(" ");
		
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		
		for (String s : participant) {
			if (map.keySet().contains(s)) {
				map.compute(s, (String, integer) -> integer+1);
			} else {
				map.put(s, 1);
			}
		}
		
		for (String s : completion) {
			if (map.keySet().contains(s)) {
				// System.out.println(s);
				map.compute(s, (String, integer) -> integer-1);
			}
			else {
				System.out.println("impossible");
			}
		}
		
		for (String s : map.keySet()) {
			if (map.get(s) > 0) {
				System.out.println(s);
			}
		}
	}

}
