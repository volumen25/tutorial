# Notes

## QR Code generator

https://gratisqr.com/

### Callouts

To cross-reference a callout, add an ID attribute that starts with the appropriate callout prefix (see Table 1). You can then reference the callout using the usual \@ syntax. For example, here we add the ID #tip-example to the callout, and then refer back to it:

::: {#tip-example .callout-tip}
## Cross-Referencing a Tip

Add an ID starting with `#tip-` to reference a tip.
:::

See @tip-example...

The prefixes for each type of callout are:

| Callout Type | Prefix  |
|--------------|---------|
| `note`       | `#nte-` |
| `tip`        | `#tip-` |
| `warning`    | `#wrn-` |
| `important`  | `#imp-` |
| `caution`    | `#cau-` |

: Prefixes for callout cross-references {#tbl-callout-prefixes}

## Equations

Provide an `#eq-` label immediately after an equation to make it referenceable. For example:

``` markdown
Black-Scholes (@eq-black-scholes) is a mathematical model that seeks to explain the behavior of financial derivatives, most commonly options:

$$
\frac{\partial \mathrm C}{ \partial \mathrm t } + \frac{1}{2}\sigma^{2} \mathrm S^{2}
\frac{\partial^{2} \mathrm C}{\partial \mathrm S^2}
  + \mathrm r \mathrm S \frac{\partial \mathrm C}{\partial \mathrm S}\ =
  \mathrm r \mathrm C 
$$ {#eq-black-scholes}
```

Black-Scholes (@eq-black-scholes) is a mathematical model that seeks to explain the behavior of financial derivatives, most commonly options:

$$
\frac{\partial \mathrm C}{ \partial \mathrm t } + \frac{1}{2}\sigma^{2} \mathrm S^{2}
\frac{\partial^{2} \mathrm C}{\partial \mathrm S^2}
  + \mathrm r \mathrm S \frac{\partial \mathrm C}{\partial \mathrm S}\ =
  \mathrm r \mathrm C 
$$ {#eq-black-scholes}

## Theorems and Proofs

Theorems are commonly used in articles and books in mathematics. To include a reference-able theorem, create a div with a `#thm-` label (or one of other theorem-type labels described below). You also need to specify a theorem name either via the first heading in the block. You can include any content you like within the div. For example:

``` markdown
::: {#thm-line}

## Line

The equation of any straight line, called a linear equation, can be written as:

$$
y = mx + b
$$
:::

See @thm-line.
```

There are a number of theorem variations supported, each with their own label prefix:

| **Label Prefix** | **Printed Name** | **LaTeX Environment** |
|------------------|------------------|-----------------------|
| `#thm-`          | Theorem          | theorem               |
| `#lem-`          | Lemma            | lemma                 |
| `#cor-`          | Corollary        | corollary             |
| `#prp-`          | Proposition      | proposition           |
| `#cnj-`          | Conjecture       | conjecture            |
| `#def-`          | Definition       | definition            |
| `#exm-`          | Example          | example               |
| `#exr-`          | Exercise         | exercise              |
| `#sol-`          | Solution         | solution              |
| `#rem-`          | Remark           | remark                |
| `#alg-`          | Algorithm        | algorithm             |