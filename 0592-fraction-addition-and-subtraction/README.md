<h2><a href="https://leetcode.com/problems/fraction-addition-and-subtraction/">592. Fraction Addition and Subtraction</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6" data-immersive-translate-paragraph="1">Given a string <code data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">expression</code> representing an expression of fraction addition and subtraction, return the calculation result in string format.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個表示分數加減表達式的字串<code data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">expression</code> ，以字串格式傳回計算結果。</font></font></font></p>

<p data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6" data-immersive-translate-paragraph="1">The final result should be an <a href="https://en.wikipedia.org/wiki/Irreducible_fraction" target="_blank" data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">irreducible fraction</a>. If your final result is an integer, change it to the format of a fraction that has a denominator <code data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">1</code>. So in this case, <code data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">2</code> should be converted to <code data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">2/1</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">最終結果應該是一個<a href="https://en.wikipedia.org/wiki/Irreducible_fraction" target="_blank" data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">不可約分數</a>。如果您的最終結果是整數，請將其變更為分母為<code data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">1</code>的分數格式。因此在這種情況下， <code data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">2</code>應轉換為<code data-immersive-translate-walked="25144382-28c4-4151-bd6e-552005f8a3f6">2/1</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> expression = "-1/2+1/2"
<strong>Output:</strong> "0/1"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> expression = "-1/2+1/2+1/3"
<strong>Output:</strong> "1/3"
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> expression = "1/3-1/2"
<strong>Output:</strong> "-1/6"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The input string only contains <code>'0'</code> to <code>'9'</code>, <code>'/'</code>, <code>'+'</code> and <code>'-'</code>. So does the output.</li>
	<li>Each fraction (input and output) has the format <code>±numerator/denominator</code>. If the first input fraction or the output is positive, then <code>'+'</code> will be omitted.</li>
	<li>The input only contains valid <strong>irreducible fractions</strong>, where the <strong>numerator</strong> and <strong>denominator</strong> of each fraction will always be in the range <code>[1, 10]</code>. If the denominator is <code>1</code>, it means this fraction is actually an integer in a fraction format defined above.</li>
	<li>The number of given fractions will be in the range <code>[1, 10]</code>.</li>
	<li>The numerator and denominator of the <strong>final result</strong> are guaranteed to be valid and in the range of <strong>32-bit</strong> int.</li>
</ul>
</div>