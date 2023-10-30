<h2><a href="https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/">1356. Sort Integers by The Number of 1 Bits<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">1356. 按 1 位數對整數進行排序</font></font></font></a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="18f6195a-3cd1-4942-9a6a-d06d195fdcea">You are given an integer array <code data-immersive-translate-effect="1" data-immersive_translate_walked="18f6195a-3cd1-4942-9a6a-d06d195fdcea">arr</code>. Sort the integers in the array&nbsp;in ascending order by the number of <code data-immersive-translate-effect="1" data-immersive_translate_walked="18f6195a-3cd1-4942-9a6a-d06d195fdcea">1</code>'s&nbsp;in their binary representation and in case of two or more integers have the same number of <code data-immersive-translate-effect="1" data-immersive_translate_walked="18f6195a-3cd1-4942-9a6a-d06d195fdcea">1</code>'s you have to sort them in ascending order.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">你得到一個整數陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="18f6195a-3cd1-4942-9a6a-d06d195fdcea">arr</code> 。按二進位表示中的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="18f6195a-3cd1-4942-9a6a-d06d195fdcea">1</code> 's 數升序對陣列中的整數進行排序，如果兩個或多個整數具有相同數量的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="18f6195a-3cd1-4942-9a6a-d06d195fdcea">1</code> '，則必須按升序對它們進行排序。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="18f6195a-3cd1-4942-9a6a-d06d195fdcea">Return <em data-immersive-translate-effect="1" data-immersive_translate_walked="18f6195a-3cd1-4942-9a6a-d06d195fdcea">the array after sorting it</em>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">排序後返回陣列。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [0,1,2,3,4,5,6,7,8]
<strong>Output:</strong> [0,1,2,4,8,3,5,6,7]
<strong>Explantion:</strong> [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [1024,512,256,128,64,32,16,8,4,2,1]
<strong>Output:</strong> [1,2,4,8,16,32,64,128,256,512,1024]
<strong>Explantion:</strong> All integers have 1 bit in the binary representation, you should just sort them in ascending order.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 500</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>