<h2><a href="https://leetcode.com/problems/flatten-nested-list-iterator/">341. Flatten Nested List Iterator</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">You are given a nested list of integers <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您將獲得一個嵌套的整數清單 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">nestedList</code> 。每個元素都是整數或清單，其元素也可以是整數或其他清單。實現反覆運算器以平展它。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">Implement the <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">NestedIterator</code> class:<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">實現 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">NestedIterator</code> 類：</font></font></font></p>

<ul>
	<li><code>NestedIterator(List&lt;NestedInteger&gt; nestedList)</code> Initializes the iterator with the nested list <code>nestedList</code>.</li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5"><code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">int next()</code> Returns the next integer in the nested list.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">int next()</code> 返回嵌套清單中的下一個整數。</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5"><code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">boolean hasNext()</code> Returns <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">true</code> if there are still some integers in the nested list and <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">false</code> otherwise.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">boolean hasNext()</code> 如果嵌套清單中 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">false</code> 仍有一些整數，則返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">true</code> 。</font></font></font></li>
</ul>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">Your code will be tested with the following pseudocode:<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您的代碼將使用以下偽代碼進行測試：</font></font></font></p>

<pre>initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
</pre>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">If <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">res</code> matches the expected flattened list, then your code will be judged as correct.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果與預期的平展清單匹配，則 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1a815d37-f7aa-4593-90c4-91461d1d46b5">res</code> 代碼將被判斷為正確。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> [1,1,2,1,1]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> [1,4,6]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 500</code></li>
	<li>The values of the integers in the nested list is in the range <code>[-10<sup>6</sup>, 10<sup>6</sup>]</code>.</li>
</ul>
</div>