/*
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
*/
class MovingAverage {
private:
    queue<int> qq;
    int maxSize;
    double sum;
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        maxSize = size;
        sum = 0;
    }
    
    double next(int val) {
        if(qq.size() == maxSize) {
            int ele = qq.front();
            sum -= ele;
            qq.pop();
        } 
        
        sum += val;
        qq.push(val);
        return sum/qq.size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */

