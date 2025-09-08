
## Z-Score
The z-score or standard score tells by how many standard deviations a value differs from the mean. This is useful when comparing values from different populations, each having their own parameters $\mu$ and $\sigma$, allowing the values to be compared in _standard units_.

$$
    z = \frac {{x} - \mu} {\sigma}
$$

Clearly, the standard score follows the same distribution as the measured values $x$ as it is simply rescaled via subtraction and division.

## Z-Test
When a hypothesis is about the _mean_ of a distribution we can use a z-test. The z-statistic is defined as follows, where $\mu_0$ is the population mean under the null hypothesis and $\sigma$ is the known (i.e. actual, real) population variance:

$$
    z = \frac {\overline{x} - \mu_0} { \sigma / \sqrt n }
$$

Fron the Central Limit Theorem we know that the sample mean $\overline{x}$ is approximately normally distributed, so the same distribution applies to the z-statistic. Note that the z-statistic in this case is essentially the same as above for the z-score; the difference between the measured value and the population mean is divided by the population standard deviation. For samples of size $n$, the standard deviation of the distribution of $\overline{x}$ is $\sigma / \sqrt{n}$.

It should be recognised that the z-test has limited practical use as it is unrealistic to think that we'd find ourselves in the situation of knowing the population variance, but not the population mean. However, it serves as a useful introduction to hypothesis testing and more powerful methods.

## Z-Table
A standard table for the z-statistic can be used for determining both critical values and p-values. Of course, software is used frequently instead of standard tables. 
Cells within the table represent the area under the standard normal curve to the left of the z-score. A standard table shows values for the standard normal cumulative distribution function:

$$
    \Phi(c) = p(z \le c) = \frac{1}{\sqrt{2\pi}}  \int\limits_{-\infty}^c  e^{-\frac{1}{2}z^2} dz
$$

We can find the probability for a value _greater than_ the critical value using:
$$
    p(z \ge c) = 1 - \Phi(z)
$$

Since the standard normal distribution is symmetric about $z = 0$ this implies that

$$ p(z \ge c) = p(-z \le -c) $$

### How to Read a Z-Table
The key to using a z-table is the following:
* Row headings define the z-score to the tenth decimal place.
* Column headings add the hundredth decimal place.

For example, to find the critical value for a z-value of 1.27, find the row in the left-most column for 1.2 and then the column on that row for 0.07; the resulting critical value is 0.8980. A sample is show at the end of this page. To use the table, we first determine the

### Test Criteria
The criteria for performing a test, for both the critical value and p-value approaches, are shown below, where $c_\alpha$ is the critical value for a significance level $\alpha$.
#### Left-Tailed Test

$$
    z \le c_\alpha \quad \text{where} \quad z, c_\alpha \lt 0 \tag{critical value approach}
$$

$$
    p(z) \le \alpha \tag{p-value approach}
$$

#### Right-Tailed Test

$$
    z \ge c_\alpha \quad \text{where} \quad z, c_\alpha \gt 0 \tag{critical value approach}
$$

$$
    p(z) \le \alpha \tag{p-value approach}
$$

#### Two-Tailed Test
For a two-tailed test the criteria depend on whether our z-value is positive or negative:
$$
    z \ge c_\alpha \quad \text{where} \quad z, c_\alpha \gt 0 \tag{critical value approach}
$$

$$
    p(z) \le \frac{\alpha}{2}  \tag{p-value approach}
$$

Or:

$$
    z \le c_\alpha \quad \text{where} \quad z, c_\alpha \lt 0 \tag{critical value approach}
$$

$$
    p(z) \le \frac{\alpha}{2}  \tag{p-value approach}
$$


#### Example
It is claimed that the mean grade for students in a university is 75. We ask, is this claim true? A random sample of grades of size 100 gives a sample mean of 73. It is known that the population standard deviation is 15.

* $H_0$ - the mean grade is 75.
* $H_A$ - the mean grade is not 75.

Calculate the z-statistic:

$$
z = \frac{73 - 75}{\frac{15}{\sqrt{100}}} = -1.33
$$

For our test we choose a significance level of 5%. Using the critical value approach, we will look up the value using a standard z-table (of course, you could use software). Since $H_A$ is about $\mu_A \ne \mu_0$ being different, which includes both $\mu_A \lt \mu_0$ and $\mu_A \gt \mu_0$, we have a two-tailed test. 

What is the critical value for a significance level of 0.05? Since we have a two-sided test the probability (significance level) is split into 0.025 for each tail of the distribution. Find the cell in the table for the probability 0.975 (i.e. $1 - 0.025$); this is row 1.9 and column 0.06. Therefore the critical value for $\alpha = 0.05$ in a two-sided test is $\pm1.96$. We perform the following check:

$$
-1.33 \le -1.96 \implies \text{false}
$$

Therefore we reject $H_A$ and accept $H_0$.

We can repeat the same test but this time use the p-value approach. Looking up the p-value from the z-table: $p(z \le 1.33) =0.9082$. Therefore $p(z \ge 1.33) = 1 - p(z \le 1.33) = 1 - 0.9082 = 0.092$. Since the standard normal distribution is symmetric about $z = 0$ we know that $p(z \ge 1.33) = p(-z \le -1.33)$. Therefore, as $ 0.092 \gt 0.05$ we reject $H_A$ and accept $H_0$.


### Appendix

#### Z-Table Sample
<table class="wikitable">
<tbody><tr>
<th><i>z</i></th>
<th>+ 0.00</th>
<th>+ 0.01</th>
<th>+ 0.02</th>
<th>+ 0.03</th>
<th>+ 0.04</th>
<th>+ 0.05</th>
<th>+ 0.06</th>
<th>+ 0.07</th>
<th>+ 0.08</th>
<th>+ 0.09
</th></tr>
<tr>
<th>0.0
</th>
<td>0.50000</td>
<td>0.50399</td>
<td>0.50798</td>
<td>0.51197</td>
<td>0.51595</td>
<td>0.51994</td>
<td>0.52392</td>
<td>0.52790</td>
<td>0.53188</td>
<td>0.53586
</td></tr>
<tr>
<th>0.1
</th>
<td>0.53983</td>
<td>0.54380</td>
<td>0.54776</td>
<td>0.55172</td>
<td>0.55567</td>
<td>0.55962</td>
<td>0.56360</td>
<td>0.56749</td>
<td>0.57142</td>
<td>0.57535
</td></tr>
<tr>
<th>0.2
</th>
<td>0.57926</td>
<td>0.58317</td>
<td>0.58706</td>
<td>0.59095</td>
<td>0.59483</td>
<td>0.59871</td>
<td>0.60257</td>
<td>0.60642</td>
<td>0.61026</td>
<td>0.61409
</td></tr>
<tr>
<th>0.3
</th>
<td>0.61791</td>
<td>0.62172</td>
<td>0.62552</td>
<td>0.62930</td>
<td>0.63307</td>
<td>0.63683</td>
<td>0.64058</td>
<td>0.64431</td>
<td>0.64803</td>
<td>0.65173
</td></tr>
<tr>
<th>0.4
</th>
<td>0.65542</td>
<td>0.65910</td>
<td>0.66276</td>
<td>0.66640</td>
<td>0.67003</td>
<td>0.67364</td>
<td>0.67724</td>
<td>0.68082</td>
<td>0.68439</td>
<td>0.68793
</td></tr>
<tr>
<td colspan="1" style="padding:0;">
</td></tr>
<tr>
<th>0.5
</th>
<td>0.69146</td>
<td>0.69497</td>
<td>0.69847</td>
<td>0.70194</td>
<td>0.70540</td>
<td>0.70884</td>
<td>0.71226</td>
<td>0.71566</td>
<td>0.71904</td>
<td>0.72240
</td></tr>
<tr>
<th>0.6
</th>
<td>0.72575</td>
<td>0.72907</td>
<td>0.73237</td>
<td>0.73565</td>
<td>0.73891</td>
<td>0.74215</td>
<td>0.74537</td>
<td>0.74857</td>
<td>0.75175</td>
<td>0.75490
</td></tr>
<tr>
<th>0.7
</th>
<td>0.75804</td>
<td>0.76115</td>
<td>0.76424</td>
<td>0.76730</td>
<td>0.77035</td>
<td>0.77337</td>
<td>0.77637</td>
<td>0.77935</td>
<td>0.78230</td>
<td>0.78524
</td></tr>
<tr>
<th>0.8
</th>
<td>0.78814</td>
<td>0.79103</td>
<td>0.79389</td>
<td>0.79673</td>
<td>0.79955</td>
<td>0.80234</td>
<td>0.80511</td>
<td>0.80785</td>
<td>0.81057</td>
<td>0.81327
</td></tr>
<tr>
<th>0.9
</th>
<td>0.81594</td>
<td>0.81859</td>
<td>0.82121</td>
<td>0.82381</td>
<td>0.82639</td>
<td>0.82894</td>
<td>0.83147</td>
<td>0.83398</td>
<td>0.83646</td>
<td>0.83891
</td></tr>
<tr>
<td colspan="1" style="padding:0;">
</td></tr>
<tr>
<th>1.0
</th>
<td>0.84134</td>
<td>0.84375</td>
<td>0.84614</td>
<td>0.84849</td>
<td>0.85083</td>
<td>0.85314</td>
<td>0.85543</td>
<td>0.85769</td>
<td>0.85993</td>
<td>0.86214
</td></tr>
<tr>
<th>1.1
</th>
<td>0.86433</td>
<td>0.86650</td>
<td>0.86864</td>
<td>0.87076</td>
<td>0.87286</td>
<td>0.87493</td>
<td>0.87698</td>
<td>0.87900</td>
<td>0.88100</td>
<td>0.88298
</td></tr>
<tr>
<th>1.2
</th>
<td>0.88493</td>
<td>0.88686</td>
<td>0.88877</td>
<td>0.89065</td>
<td>0.89251</td>
<td>0.89435</td>
<td>0.89617</td>
<td>0.89796</td>
<td>0.89973</td>
<td>0.90147
</td></tr>
<tr>
<th>1.3
</th>
<td>0.90320</td>
<td>0.90490</td>
<td>0.90658</td>
<td>0.90824</td>
<td>0.90988</td>
<td>0.91149</td>
<td>0.91308</td>
<td>0.91466</td>
<td>0.91621</td>
<td>0.91774
</td></tr>
<tr>
<th>1.4
</th>
<td>0.91924</td>
<td>0.92073</td>
<td>0.92220</td>
<td>0.92364</td>
<td>0.92507</td>
<td>0.92647</td>
<td>0.92785</td>
<td>0.92922</td>
<td>0.93056</td>
<td>0.93189
</td></tr>
<tr>
<td colspan="1" style="padding:0;">
</td></tr>
<tr>
<th>1.5
</th>
<td>0.93319</td>
<td>0.93448</td>
<td>0.93574</td>
<td>0.93699</td>
<td>0.93822</td>
<td>0.93943</td>
<td>0.94062</td>
<td>0.94179</td>
<td>0.94295</td>
<td>0.94408
</td></tr>
<tr>
<th>1.6
</th>
<td>0.94520</td>
<td>0.94630</td>
<td>0.94738</td>
<td>0.94845</td>
<td>0.94950</td>
<td>0.95053</td>
<td>0.95154</td>
<td>0.95254</td>
<td>0.95352</td>
<td>0.95449
</td></tr>
<tr>
<th>1.7
</th>
<td>0.95543</td>
<td>0.95637</td>
<td>0.95728</td>
<td>0.95818</td>
<td>0.95907</td>
<td>0.95994</td>
<td>0.96080</td>
<td>0.96164</td>
<td>0.96246</td>
<td>0.96327
</td></tr>
<tr>
<th>1.8
</th>
<td>0.96407</td>
<td>0.96485</td>
<td>0.96562</td>
<td>0.96638</td>
<td>0.96712</td>
<td>0.96784</td>
<td>0.96856</td>
<td>0.96926</td>
<td>0.96995</td>
<td>0.97062
</td></tr>
<tr>
<th>1.9
</th>
<td>0.97128</td>
<td>0.97193</td>
<td>0.97257</td>
<td>0.97320</td>
<td>0.97381</td>
<td>0.97441</td>
<td>0.97500</td>
<td>0.97558</td>
<td>0.97615</td>
<td>0.97670
</td></tr>
<tr>
<td colspan="1" style="padding:0;">
</td></tr>
<tr>
<th>2.0
</th>
<td>0.97725</td>
<td>0.97778</td>
<td>0.97831</td>
<td>0.97882</td>
<td>0.97932</td>
<td>0.97982</td>
<td>0.98030</td>
<td>0.98077</td>
<td>0.98124</td>
<td>0.98169
</td></tr>
<tr>
<th>2.1
</th>
<td>0.98214</td>
<td>0.98257</td>
<td>0.98300</td>
<td>0.98341</td>
<td>0.98382</td>
<td>0.98422</td>
<td>0.98461</td>
<td>0.98500</td>
<td>0.98537</td>
<td>0.98574
</td></tr>
<tr>
<th>2.2
</th>
<td>0.98610</td>
<td>0.98645</td>
<td>0.98679</td>
<td>0.98713</td>
<td>0.98745</td>
<td>0.98778</td>
<td>0.98809</td>
<td>0.98840</td>
<td>0.98870</td>
<td>0.98899
</td></tr>
<tr>
<th>2.3
</th>
<td>0.98928</td>
<td>0.98956</td>
<td>0.98983</td>
<td>0.99010</td>
<td>0.99036</td>
<td>0.99061</td>
<td>0.99086</td>
<td>0.99111</td>
<td>0.99134</td>
<td>0.99158
</td></tr>
<tr>
<th>2.4
</th>
<td>0.99180</td>
<td>0.99202</td>
<td>0.99224</td>
<td>0.99245</td>
<td>0.99266</td>
<td>0.99286</td>
<td>0.99305</td>
<td>0.99324</td>
<td>0.99343</td>
<td>0.99361
</td></tr>
<tr>
<td colspan="1" style="padding:0;">
</td></tr>
<tr>
<th>2.5
</th>
<td>0.99379</td>
<td>0.99396</td>
<td>0.99413</td>
<td>0.99430</td>
<td>0.99446</td>
<td>0.99461</td>
<td>0.99477</td>
<td>0.99492</td>
<td>0.99506</td>
<td>0.99520
</td></tr>
<tr>
<th>2.6
</th>
<td>0.99534</td>
<td>0.99547</td>
<td>0.99560</td>
<td>0.99573</td>
<td>0.99585</td>
<td>0.99598</td>
<td>0.99609</td>
<td>0.99621</td>
<td>0.99632</td>
<td>0.99643
</td></tr>
<tr>
<th>2.7
</th>
<td>0.99653</td>
<td>0.99664</td>
<td>0.99674</td>
<td>0.99683</td>
<td>0.99693</td>
<td>0.99702</td>
<td>0.99711</td>
<td>0.99720</td>
<td>0.99728</td>
<td>0.99736
</td></tr>
<tr>
<th>2.8
</th>
<td>0.99744</td>
<td>0.99752</td>
<td>0.99760</td>
<td>0.99767</td>
<td>0.99774</td>
<td>0.99781</td>
<td>0.99788</td>
<td>0.99795</td>
<td>0.99801</td>
<td>0.99807
</td></tr>
<tr>
<th>2.9
</th>
<td>0.99813</td>
<td>0.99819</td>
<td>0.99825</td>
<td>0.99831</td>
<td>0.99836</td>
<td>0.99841</td>
<td>0.99846</td>
<td>0.99851</td>
<td>0.99856</td>
<td>0.99861
</td></tr>
<tr>
<td colspan="1" style="padding:0;">
</td></tr>
<tr>
<th>3.0
</th>
<td>0.99865</td>
<td>0.99869</td>
<td>0.99874</td>
<td>0.99878</td>
<td>0.99882</td>
<td>0.99886</td>
<td>0.99889</td>
<td>0.99893</td>
<td>0.99896</td>
<td>0.99900
</td></tr>
<tr>
<th>3.1
</th>
<td>0.99903</td>
<td>0.99906</td>
<td>0.99910</td>
<td>0.99913</td>
<td>0.99916</td>
<td>0.99918</td>
<td>0.99921</td>
<td>0.99924</td>
<td>0.99926</td>
<td>0.99929
</td></tr>
<tr>
<th>3.2
</th>
<td>0.99931</td>
<td>0.99934</td>
<td>0.99936</td>
<td>0.99938</td>
<td>0.99940</td>
<td>0.99942</td>
<td>0.99944</td>
<td>0.99946</td>
<td>0.99948</td>
<td>0.99950
</td></tr>
<tr>
<th>3.3
</th>
<td>0.99952</td>
<td>0.99953</td>
<td>0.99955</td>
<td>0.99957</td>
<td>0.99958</td>
<td>0.99960</td>
<td>0.99961</td>
<td>0.99962</td>
<td>0.99964</td>
<td>0.99965
</td></tr>
<tr>
<th>3.4
</th>
<td>0.99966</td>
<td>0.99968</td>
<td>0.99969</td>
<td>0.99970</td>
<td>0.99971</td>
<td>0.99972</td>
<td>0.99973</td>
<td>0.99974</td>
<td>0.99975</td>
<td>0.99976
</td></tr>
<tr>
<td colspan="1" style="padding:0;">
</td></tr>
<tr>
<th>3.5
</th>
<td>0.99977</td>
<td>0.99978</td>
<td>0.99978</td>
<td>0.99979</td>
<td>0.99980</td>
<td>0.99981</td>
<td>0.99981</td>
<td>0.99982</td>
<td>0.99983</td>
<td>0.99983
</td></tr>
<tr>
<th>3.6
</th>
<td>0.99984</td>
<td>0.99985</td>
<td>0.99985</td>
<td>0.99986</td>
<td>0.99986</td>
<td>0.99987</td>
<td>0.99987</td>
<td>0.99988</td>
<td>0.99988</td>
<td>0.99989
</td></tr>
<tr>
<th>3.7
</th>
<td>0.99989</td>
<td>0.99990</td>
<td>0.99990</td>
<td>0.99990</td>
<td>0.99991</td>
<td>0.99991</td>
<td>0.99992</td>
<td>0.99992</td>
<td>0.99992</td>
<td>0.99992
</td></tr>
<tr>
<th>3.8
</th>
<td>0.99993</td>
<td>0.99993</td>
<td>0.99993</td>
<td>0.99994</td>
<td>0.99994</td>
<td>0.99994</td>
<td>0.99994</td>
<td>0.99995</td>
<td>0.99995</td>
<td>0.99995
</td></tr>
<tr>
<th>3.9
</th>
<td>0.99995</td>
<td>0.99995</td>
<td>0.99996</td>
<td>0.99996</td>
<td>0.99996</td>
<td>0.99996</td>
<td>0.99996</td>
<td>0.99996</td>
<td>0.99997</td>
<td>0.99997
</td></tr>
<tr>
<td colspan="1" style="padding:0;">
</td></tr>
<tr>
<th>4.0
</th>
<td>0.99997</td>
<td>0.99997</td>
<td>0.99997</td>
<td>0.99997</td>
<td>0.99997</td>
<td>0.99997</td>
<td>0.99998</td>
<td>0.99998</td>
<td>0.99998</td>
<td>0.99998
</td></tr>
<tr>
<th><i>z</i></th>
<th>+0.00</th>
<th>+0.01</th>
<th>+0.02</th>
<th>+0.03</th>
<th>+0.04</th>
<th>+0.05</th>
<th>+0.06</th>
<th>+0.07</th>
<th>+0.08</th>
<th>+0.09
</th></tr></tbody></table>