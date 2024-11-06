<h2><a href="https://leetcode.com/problems/find-if-array-can-be-sorted/">3011. Find if Array Can Be Sorted</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2" data-immersive-translate-paragraph="1">You are given a <strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">0-indexed</strong> array of <strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">positive</strong> integers <code data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">nums</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給您一個<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">0 索引</strong>的<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">正</strong>整數數組<code data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">nums</code> 。</font></font></font></p>

<p data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2" data-immersive-translate-paragraph="1">In one <strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">operation</strong>, you can swap any two <strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">adjacent</strong> elements if they have the <strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">same</strong> number of <span data-keyword="set-bit" data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">set bits</span>. You are allowed to do this operation <strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">any</strong> number of times (<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">including zero</strong>).<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">在一項<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">操作</strong>中，如果任兩個<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">相鄰</strong>元素具有<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">相同</strong>的<span data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2" data-keyword="set-bit">設定</span>位數，則可以交換它們。您可以執行此操作<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">任意</strong>次數（<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">包括零次</strong>）。</font></font></font></p>

<p data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2" data-immersive-translate-paragraph="1">Return <code data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">true</code> <em data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">if you can sort the array, else return </em><code data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">false</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><em data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">如果可以對陣列進行排序，則</em>傳回<code data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">true</code> ，否則傳回<code data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">false</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2" data-immersive-translate-paragraph="1"><strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">Input:</strong> nums = [8,4,2,30,15]
<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">Output:</strong> true
<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">Explanation:</strong> Let's look at the binary representation of every element. The numbers 2, 4, and 8 have one set bit each with binary representation "10", "100", and "1000" respectively. The numbers 15 and 30 have four set bits each with binary representation "1111" and "11110".
We can sort the array using 4 operations:
- Swap nums[0] with nums[1]. This operation is valid because 8 and 4 have one set bit each. The array becomes [4,8,2,30,15].
- Swap nums[1] with nums[2]. This operation is valid because 8 and 2 have one set bit each. The array becomes [4,2,8,30,15].
- Swap nums[0] with nums[1]. This operation is valid because 4 and 2 have one set bit each. The array becomes [2,4,8,30,15].
- Swap nums[3] with nums[4]. This operation is valid because 30 and 15 have four set bits each. The array becomes [2,4,8,15,30].
The array has become sorted, hence we return true.
Note that there may be other sequences of operations which also sort the array.
<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-pre-whitespace immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">輸入：</strong> nums = [8,4,2,30,15]
<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">輸出：</strong>真
<strong data-immersive-translate-walked="79cce675-ac2f-41bd-84e9-01d28ed564b2">說明：</strong>讓我們看一下每個元素的二進位表示。數字2、4和8分別具有一組二進位表示「10」、「100」和「1000」的位元。數字15和30具有四個設定位，每個設定位具有二進位表示「1111」和「11110」。
我們可以使用 4 個操作對陣列進行排序：
- 將 nums[0] 與 nums[1] 交換。操作有效，因為 8 和 4 各有一個設定位。數組變成 [4,8,2,30,15]。
- 將 nums[1] 與 nums[2] 交換。此操作有效，因為 8 和 2 各有一個設定位。數組變為 [4,2,8,30,15]。
- 將 nums[0] 與 nums[1] 交換。操作有效，因為 4 和 2 各有一個設定位。數組變為 [2,4,8,30,15]。
- 將 nums[3] 與 nums[4] 交換。此操作有效，因為 30 和 15 各有四個設定位。數組變為 [2,4,8,15,30]。
數組已排序，因此我們傳回 true。
請注意，可能還有其他操作序列也會對陣列進行排序。</font></font></font></pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> The array is already sorted, hence we return true.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3,16,8,4,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> It can be shown that it is not possible to sort the input array using any number of operations.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2<sup>8</sup></code></li>
</ul>
</div>