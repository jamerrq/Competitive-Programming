import java.util.*;

class The_Department_of_Redundancy_Department
{
	public static void main (String[] args) throws java.lang.Exception
	{
		ArrayList<Integer> a = new ArrayList<>();
		Scanner s = new Scanner(System.in);
		while(s.hasNextInt()){
			String n = s.next();
			int b = Integer.parseInt(n);
			a.add(b);
		}
		int[] nums = new int[a.size()];
		for(int i = 0; i < a.size(); i++){
			nums[i] = a.get(i);
		}
		Map<Integer, Integer> m = new HashMap<Integer, Integer>();
		for(int i = 0; i < nums.length; i++){
			if(!m.containsKey(nums[i])){
				int count = 0;
				for(int j = 0; j < nums.length; j++){
					if(nums[i] == nums[j])count++;
				}
				m.put(nums[i], count);
				System.out.println(nums[i] + " " + count);
			}
		}
		s.close();
	}
}
