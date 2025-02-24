import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'O Painel e-SUS APS',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        É um software gratuito e integrado à base de dados local do sistema e-SUS APS. Destinado aos profissionais da assistência e gestão em saúde e focado na implementação de boas práticas.
      </>
    ),
  },
  {
    title: 'Relatórios Temáticos',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
       Reúne dados populacionais e de saúde, permitindo uma compreensão atualizada das condições do território, além de um acompanhamento longitudinal e integrado dos cidadãos cadastrados.
       </>
    ),
  },
  {
    title: 'Lista Nominal',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
       As lista nominais são recursos fundamentais para apoio da busca ativa e identificação da população acompanhada. Os alertas sobre a situação das boas práticas a serem monitoradas pela a equipe de saúde.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
