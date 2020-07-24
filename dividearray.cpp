/*

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
*/

class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        if (nums.size()%k != 0) {
            return false;
        }
        
        map<int, int> mymap;
        
        for(int i = 0; i < nums.size(); i++) {
            map<int, int>::iterator it = mymap.find(nums[i]);
            if ( it != mymap.end()) {
                mymap[nums[i]] += 1;
            }
            else {
                mymap[nums[i]] = 1;
            }
        }
        
        int v = 0, count = 0, prev = -1;
        for(map<int,int>::iterator it=mymap.begin();  it != mymap.end(); it++) {
            if(count >= k) {
                prev = -1;
                count = 0;
                it = mymap.begin();
            } 
            if( prev != -1 && (prev+1) != it->first) {
                return false;
            }
            prev = it->first;
            if (it->second == 1) {
                mymap.erase(it);
              
            } else{
                it->second--;
            }
            count++;
            
        }
        if (count == k) {
            return true;
        }
        return false;
    }
};
