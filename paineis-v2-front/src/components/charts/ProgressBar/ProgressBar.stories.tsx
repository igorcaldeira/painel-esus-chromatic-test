import type { Meta, StoryObj } from '@storybook/react';
import { ProgressBar } from './index';

const meta = {
  title: 'Charts/ProgressBar (Em Andamento)',
  component: ProgressBar,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
  args: { 
},
} satisfies Meta<typeof ProgressBar>;

export default meta;
type Story = StoryObj<typeof meta>;


export const Primary: Story = {
  args: {
    data: [
      {
        tag: "urbano",
        value: 81,
      },
      {
        tag: "nao-informado",
        value: 20,
      },
      {
        tag: "rural",
        value: 19,
      },
    ]
  },
};