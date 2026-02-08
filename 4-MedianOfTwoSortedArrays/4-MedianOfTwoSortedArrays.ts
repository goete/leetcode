// Last updated: 2/8/2026, 12:03:53 AM
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    let merged = nums1.concat(nums2);
    merged.sort((a, b) => a - b);

    let n = Math.floor(merged.length / 2);
    if (merged.length % 2 === 1) {
        return merged[n];
    } else {
        return (merged[n] + merged[n - 1]) / 2;
    }
};