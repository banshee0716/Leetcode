<h2><a href="https://leetcode.com/problems/maximum-xor-for-each-query/">1829. Maximum XOR for Each Query</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5" data-immersive-translate-paragraph="1">You are given a <strong data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">sorted</strong> array <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">nums</code> of <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">n</code> non-negative integers and an integer <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">maximumBit</code>. You want to perform the following query <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">n</code> <strong data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">times</strong>:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給您一個由<code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">n</code>非負整數組成的<strong data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">排序</strong>數組<code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">nums</code>和一個整數<code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">maximumBit</code> 。您想要執行以下查詢<code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">n</code><strong data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">次</strong>：</font></font></font></p>

<ol>
	<li data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5" data-immersive-translate-paragraph="1">Find a non-negative integer <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">k &lt; 2<sup>maximumBit</sup></code> such that <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k</code> is <strong data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">maximized</strong>. <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">k</code> is the answer to the <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">i<sup>th</sup></code> query.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">找出一個非負整數<code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">k &lt; 2 <sup>maximumBit</sup></code> ，使得 <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k</code> 已<strong data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">最大化</strong>。 <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">k</code>是<code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">i <sup>th</sup></code>查詢的答案。</font></font></font></li>
	<li data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5" data-immersive-translate-paragraph="1">Remove the <strong data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">last </strong>element from the current array <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">nums</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">從目前數組<code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">nums</code>中刪除<strong data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">最後一個</strong>元素。</font></font></font></li>
</ol>

<p data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">an array</em> <code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">answer</code><em data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">, where </em><code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">answer[i]</code><em data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5"> is the answer to the </em><code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">i<sup>th</sup></code><em data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5"> query</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回<em data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">一個陣列</em><code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">answer</code> <em data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">，其中</em><code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">answer[i]</code>是<code data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5"><sup>i th</sup></code><em data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">查詢</em><em data-immersive-translate-walked="ee8efbbc-dd21-4739-bffe-150b830ac0c5">的答案</em>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,1,3], maximumBit = 2
<strong>Output:</strong> [0,3,2,3]
<strong>Explanation</strong>: The queries are answered as follows:
1<sup>st</sup> query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
2<sup>nd</sup> query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
3<sup>rd</sup> query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
4<sup>th</sup> query: nums = [0], k = 3 since 0 XOR 3 = 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,3,4,7], maximumBit = 3
<strong>Output:</strong> [5,2,6,5]
<strong>Explanation</strong>: The queries are answered as follows:
1<sup>st</sup> query: nums = [2,3,4,7], k = 5 since 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7.
2<sup>nd</sup> query: nums = [2,3,4], k = 2 since 2 XOR 3 XOR 4 XOR 2 = 7.
3<sup>rd</sup> query: nums = [2,3], k = 6 since 2 XOR 3 XOR 6 = 7.
4<sup>th</sup> query: nums = [2], k = 5 since 2 XOR 5 = 7.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,2,2,5,7], maximumBit = 3
<strong>Output:</strong> [4,3,6,4,6,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= maximumBit &lt;= 20</code></li>
	<li><code>0 &lt;= nums[i] &lt; 2<sup>maximumBit</sup></code></li>
	<li><code>nums</code>​​​ is sorted in <strong>ascending</strong> order.</li>
</ul>
</div>