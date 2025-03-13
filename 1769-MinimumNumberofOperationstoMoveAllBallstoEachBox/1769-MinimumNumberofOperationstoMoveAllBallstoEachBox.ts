function minOperations(boxes: string): number[] {
    const length : number = boxes.length;
    const ans : number[] = new Array(length).fill(0);
    const nums: number[] = boxes.split('').map(char => Number(char));
    for (let i :number = 0; i < length; i++) {
        ans[i] = movement(nums, i);
    }
    return ans;
};

function movement(nums : number[], pos : number): number {
    let ans : number = 0;
    for (let i :number = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            ans += Math.abs(pos - i);
        }
    }
    return ans;
};