<h2><a href="https://leetcode.com/problems/hand-of-straights/">846. Hand of Straights</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">groupSize</code>, and consists of <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">groupSize</code> consecutive cards.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">愛麗絲有一些牌，她想把牌重新排列成組，這樣每組的大小都是， <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">groupSize</code> 並且由 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">groupSize</code> 連續的牌組成。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">Given an integer array <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">hand</code> where <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">hand[i]</code> is the value written on the <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">i<sup>th</sup></code> card and an integer <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">groupSize</code>, return <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">true</code> if she can rearrange the cards, or <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">false</code> otherwise.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">hand</code> ，其中 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">hand[i]</code> 寫在卡片上的值和一個整數 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">groupSize</code> ，如果她可以重新排列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">i<sup>th</sup></code> 卡片， <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">false</code> 則返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a8149f65-ad2a-476e-b10d-e4ef381ce748">true</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> hand = [1,2,3,4,5], groupSize = 4
<strong>Output:</strong> false
<strong>Explanation:</strong> Alice's hand can not be rearranged into groups of 4.

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hand.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= hand[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= groupSize &lt;= hand.length</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1296: <a href="https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/" target="_blank">https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/</a></p>
</div>