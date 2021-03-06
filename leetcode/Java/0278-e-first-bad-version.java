/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

/*
 * Binary Search
 */
public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int start = 1, end = n;
        int mid;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (isBadVersion(mid))
                end = mid;
            else
                start = mid;
        }
        if (isBadVersion(start))
            return start;
        else
            return end;
    }
}