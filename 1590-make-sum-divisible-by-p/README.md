<h2><a href="https://leetcode.com/problems/make-sum-divisible-by-p/">1590. Make Sum Divisible by P</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12" data-immersive-translate-paragraph="1">Given an array of positive integers <code data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">nums</code>, remove the <strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">smallest</strong> subarray (possibly <strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">empty</strong>) such that the <strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">sum</strong> of the remaining elements is divisible by <code data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">p</code>. It is <strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">not</strong> allowed to remove the whole array.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個正整數數組<code data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">nums</code> ，刪除<strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">最小的</strong>子數組（可能為<strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">空</strong>），使得剩餘元素的<strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">總和</strong>可被<code data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">p</code>整除。<strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">不允許</strong>刪除整個數組。</font></font></font></p>

<p data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">the length of the smallest subarray that you need to remove, or </em><code data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">-1</code><em data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12"> if it's impossible</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回<em data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">需要刪除的最小子數組的長度，</em><em data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">如果不可能，</em>則傳回<code data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">-1</code> 。</font></font></font></p>

<p data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12" data-immersive-translate-paragraph="1">A <strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">subarray</strong> is defined as a contiguous block of elements in the array.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">子數組</strong>被定義為數組中連續的元素塊。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12" data-immersive-translate-paragraph="1"><strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">Input:</strong> nums = [3,1,4,2], p = 6
<strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">Output:</strong> 1
<strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">Explanation:</strong> The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-pre-whitespace immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">輸入：</strong> nums = [3,1,4,2]，p = 6
<strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">輸出：</strong> 1
<strong data-immersive-translate-walked="bc038a20-f387-4655-9ae8-c3463b4ceb12">解釋：</strong> nums 中元素的和為 10，不能被 6 整除。</font></font></font></pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [6,3,5,2], p = 9
<strong>Output:</strong> 2
<strong>Explanation:</strong> We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3], p = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= p &lt;= 10<sup>9</sup></code></li>
</ul>
</div>