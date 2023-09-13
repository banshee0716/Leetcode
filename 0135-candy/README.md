<h2><a href="https://leetcode.com/problems/candy/">135. Candy</a></h2><h3>Hard</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">There are <code data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">ratings</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">有 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">n</code> 孩子站成一排。每個孩子都被分配一個在整數數位 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">ratings</code> 中給出的評級值。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">You are giving candies to these children subjected to the following requirements:<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您向這些孩子贈送糖果，但須符合以下要求：</font></font></font></p>

<ul>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">Each child must have at least one candy.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">每個孩子必須至少吃一顆糖果。</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">Children with a higher rating get more candies than their neighbors.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">評分較高的孩子比鄰居得到更多的糖果。</font></font></font></li>
</ul>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">Return <em data-immersive-translate-effect="1" data-immersive_translate_walked="a473b2da-0afa-415f-b4f7-faba6b0d3c3f">the minimum number of candies you need to have to distribute the candies to the children</em>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">退回將糖果分發給孩子們所需的最少數量的糖果。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> ratings = [1,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> ratings = [1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == ratings.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>
</div>