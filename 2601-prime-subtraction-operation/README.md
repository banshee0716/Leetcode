<h2><a href="https://leetcode.com/problems/prime-subtraction-operation/">2601. Prime Subtraction Operation</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692" data-immersive-translate-paragraph="1">You are given a <strong data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">0-indexed</strong> integer array <code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">nums</code> of length <code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">n</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個長度為<code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">n</code>的<strong data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">0 索引</strong>整數數組<code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">nums</code> 。</font></font></font></p>

<p data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692" data-immersive-translate-paragraph="1">You can perform the following operation as many times as you want:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您可以根據需要執行以下操作：</font></font></font></p>

<ul>
	<li data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692" data-immersive-translate-paragraph="1">Pick an index <code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">i</code> that you haven’t picked before, and pick a prime <code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">p</code> <strong data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">strictly less than</strong> <code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">nums[i]</code>, then subtract <code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">p</code> from <code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">nums[i]</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">選擇一個之前沒有選擇的索引<code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">i</code> ，然後選擇一個<strong data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">嚴格小於</strong><code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">nums[i]</code>質數<code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">p</code> ，然後從<code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">nums[i]</code>中減去<code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">p</code> 。</font></font></font></li>
</ul>

<p data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">true if you can make <code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">nums</code> a strictly increasing array using the above operation and false otherwise.</em><font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><em data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">如果可以使用上述操作使<code data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">nums</code>成為嚴格遞增的數組，則傳回 true，否則傳回 false。</em></font></font></font></p>

<p data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692" data-immersive-translate-paragraph="1">A <strong data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">strictly increasing array</strong> is an array whose each element is strictly greater than its preceding element.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="f866cdbe-6602-4707-9028-d335acead692">嚴格遞增數組</strong>是指每個元素都嚴格大於其前一個元素的數組。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [4,9,6,10]
<strong>Output:</strong> true
<strong>Explanation:</strong> In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [6,8,11,12]
<strong>Output:</strong> true
<strong>Explanation: </strong>Initially nums is sorted in strictly increasing order, so we don't need to make any operations.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [5,8,3]
<strong>Output:</strong> false
<strong>Explanation:</strong> It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code><font face="monospace">nums.length == n</font></code></li>
</ul>
</div>