"""store prepTime and cookTime; rename time to totalTime

Revision ID: 67f451699e84
Revises: ade6487fe28a
Create Date: 2022-10-10 00:37:11.797688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67f451699e84'
down_revision = 'ade6487fe28a'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prepTime', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('cookTime', sa.Integer(), nullable=True))
        batch_op.alter_column('time', new_column_name='totalTime')



def downgrade():
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.alter_column('totalTime', new_column_name='time')
        batch_op.drop_column('cookTime')
        batch_op.drop_column('prepTime')
