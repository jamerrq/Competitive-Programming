public class Sok
{
    public static void main(String[] args){
    	java.util.Scanner sc = new java.util.Scanner(System.in);
    	double A = sc.nextDouble(), B = sc.nextDouble(), C = sc.nextDouble();
    	double a = sc.nextDouble(), b = sc.nextDouble(), c = sc.nextDouble();
    	double ra = A / a, rb = B / b, rc = C / c;
    	double rmin = Math.min(ra, Math.min(rb, rc));
    	double ca = A - (a * rmin), cb = B - (b * rmin), cc = C - (c * rmin);
		System.out.println(ca + " " + cb + " " + cc);
		sc.close();
    }
}
