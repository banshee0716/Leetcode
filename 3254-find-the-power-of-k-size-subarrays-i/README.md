<h2><a href="https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/">3254. Find the Power of K-Size Subarrays I</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4" data-immersive-translate-paragraph="1">You are given an array of integers <code data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">nums</code> of length <code data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">n</code> and a <em data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">positive</em> integer <code data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">k</code>.</p>

<p data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4" data-immersive-translate-paragraph="1">The <strong data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">power</strong> of an array is defined as:</p>

<ul>
	<li data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4" data-immersive-translate-paragraph="1">Its <strong data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">maximum</strong> element if <em data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">all</em> of its elements are <strong data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">consecutive</strong> and <strong data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">sorted</strong> in <strong data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">ascending</strong> order.</li>
	<li data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4" data-immersive-translate-paragraph="1">-1 otherwise.</li>
</ul>

<p data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4" data-immersive-translate-paragraph="1">You need to find the <strong data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">power</strong> of all <span data-keyword="subarray-nonempty" data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">subarrays</span> of <code data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">nums</code> of size <code data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">k</code>.</p>

<p data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4" data-immersive-translate-paragraph="1">Return an integer array <code data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">results</code> of size <code data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">n - k + 1</code>, where <code data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">results[i]</code> is the <em data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">power</em> of <code data-immersive-translate-walked="8f08a553-a1f0-4252-be9e-ec88e5edcee4">nums[i..(i + k - 1)]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,3,2,5], k = 3</span></p>

<p><strong>Output:</strong> [3,4,-1,-1,-1]</p>

<p><strong>Explanation:</strong></p>

<p>There are 5 subarrays of <code>nums</code> of size 3:</p>

<ul>
	<li><code>[1, 2, 3]</code> with the maximum element 3.</li>
	<li><code>[2, 3, 4]</code> with the maximum element 4.</li>
	<li><code>[3, 4, 3]</code> whose elements are <strong>not</strong> consecutive.</li>
	<li><code>[4, 3, 2]</code> whose elements are <strong>not</strong> sorted.</li>
	<li><code>[3, 2, 5]</code> whose elements are <strong>not</strong> consecutive.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,2,2,2], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,-1]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,3,2,3,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,3,-1,3,-1]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>
</div>