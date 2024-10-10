<h2><a href="https://leetcode.com/problems/maximum-width-ramp/">962. Maximum Width Ramp</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce" data-immersive-translate-paragraph="1">A <strong data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">ramp</strong> in an integer array <code data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">nums</code> is a pair <code data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">(i, j)</code> for which <code data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">i &lt; j</code> and <code data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">nums[i] &lt;= nums[j]</code>. The <strong data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">width</strong> of such a ramp is <code data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">j - i</code>.</p>

<p data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce" data-immersive-translate-paragraph="1">Given an integer array <code data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">nums</code>, return <em data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">the maximum width of a <strong data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">ramp</strong> in </em><code data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">nums</code>. If there is no <strong data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">ramp</strong> in <code data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">nums</code>, return <code data-immersive-translate-walked="c636ea47-372a-4264-8b4c-a203fa53a9ce">0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [6,0,8,2,1,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [9,8,1,0,1,9,4,0,4,1]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
</ul>
</div>