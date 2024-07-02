<h2><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii/">350. Intersection of Two Arrays II</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-walked="b494ea8d-66ef-4444-9008-c5506f0de780" data-immersive-translate-paragraph="1">Given two integer arrays <code data-immersive-translate-walked="b494ea8d-66ef-4444-9008-c5506f0de780">nums1</code> and <code data-immersive-translate-walked="b494ea8d-66ef-4444-9008-c5506f0de780">nums2</code>, return <em data-immersive-translate-walked="b494ea8d-66ef-4444-9008-c5506f0de780">an array of their intersection</em>. Each element in the result must appear as many times as it shows in both arrays and you may return the result in <strong data-immersive-translate-walked="b494ea8d-66ef-4444-9008-c5506f0de780">any order</strong>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定兩個整數數組 <code data-immersive-translate-walked="b494ea8d-66ef-4444-9008-c5506f0de780">nums1</code> 和 <code data-immersive-translate-walked="b494ea8d-66ef-4444-9008-c5506f0de780">nums2</code> ，傳回它們交集的陣列。結果中的每個元素出現的次數必須與它在兩個數組中顯示的次數相同，並且您可以按任意順序傳回結果。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [4,9]
<strong>Explanation:</strong> [9,4] is also accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>What if the given array is already sorted? How would you optimize your algorithm?</li>
	<li>What if <code>nums1</code>'s size is small compared to <code>nums2</code>'s size? Which algorithm is better?</li>
	<li>What if elements of <code>nums2</code> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>
</div>