<h2><a href="https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/">1574. Shortest Subarray to be Removed to Make Array Sorted</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416" data-immersive-translate-paragraph="1">Given an integer array <code data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">arr</code>, remove a subarray (can be empty) from <code data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">arr</code> such that the remaining elements in <code data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">arr</code> are <strong data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">non-decreasing</strong>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數數組<code data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">arr</code> ，從<code data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">arr</code>中刪除一個子數組（可以為空），使得<code data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">arr</code>中的剩餘元素是非<strong data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">遞減的</strong>。</font></font></font></p>

<p data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">the length of the shortest subarray to remove</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回<em data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">要刪除的最短子數組的長度</em>。</font></font></font></p>

<p data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416" data-immersive-translate-paragraph="1">A <strong data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">subarray</strong> is a contiguous subsequence of the array.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="771d5533-b3e2-472b-b316-1b9c5212b416">子數組</strong>是數組的連續子序列。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [1,2,3,10,4,2,3,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [5,4,3,2,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> arr = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The array is already non-decreasing. We do not need to remove any elements.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>